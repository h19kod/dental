/**
 * DENTAL PRO - Main JavaScript
 * نظام إدارة عيادة الأسنان
 */

// API Base URL
const API_BASE_URL = '/api';

// Utility Functions
const utils = {
    /**
     * Format date to Arabic locale
     */
    formatDate: (dateString) => {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(dateString).toLocaleDateString('ar-SA', options);
    },

    /**
     * Format time to 12-hour format
     */
    formatTime: (timeString) => {
        const [hours, minutes] = timeString.split(':');
        const date = new Date();
        date.setHours(hours, minutes);
        return date.toLocaleTimeString('ar-SA', { hour: '2-digit', minute: '2-digit' });
    },

    /**
     * Get status badge HTML
     */
    getStatusBadge: (status) => {
        const statusMap = {
            'PENDING': { class: 'badge-pending', text: 'قيد الانتظار' },
            'CONFIRMED': { class: 'badge-confirmed', text: 'تم التأكيد' },
            'COMPLETED': { class: 'badge-completed', text: 'تمت الزيارة' },
            'CANCELLED': { class: 'badge-cancelled', text: 'ملغي' }
        };
        const statusInfo = statusMap[status] || { class: 'badge-pending', text: status };
        return `<span class="badge ${statusInfo.class}">${statusInfo.text}</span>`;
    },

    /**
     * Show loading spinner
     */
    showLoading: (elementId) => {
        const element = document.getElementById(elementId);
        if (element) {
            element.innerHTML = '<div class="d-flex justify-content-center"><div class="spinner"></div></div>';
        }
    },

    /**
     * Handle API errors
     */
    handleError: (error, message = 'حدث خطأ في الاتصال') => {
        console.error('API Error:', error);
        alert(message);
    }
};

// Appointment Management
const appointmentManager = {
    /**
     * Fetch appointments with optional search
     */
    async fetchAppointments(searchQuery = '') {
        try {
            const url = searchQuery 
                ? `${API_BASE_URL}/appointments/?search=${encodeURIComponent(searchQuery)}`
                : `${API_BASE_URL}/appointments/`;
            
            const response = await fetch(url);
            if (!response.ok) throw new Error('Failed to fetch appointments');
            
            const data = await response.json();
            return data;
        } catch (error) {
            utils.handleError(error, 'فشل في تحميل المواعيد');
            return [];
        }
    },

    /**
     * Delete an appointment
     */
    async deleteAppointment(id) {
        if (!confirm('هل أنت متأكد من حذف هذا الموعد؟')) return;
        
        try {
            const response = await fetch(`${API_BASE_URL}/appointments/${id}/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': this.getCsrfToken()
                }
            });
            
            if (!response.ok) throw new Error('Failed to delete appointment');
            
            // Refresh the appointments list
            dashboardApp.loadAppointments();
            
            // Show success message
            this.showNotification('تم حذف الموعد بنجاح', 'success');
        } catch (error) {
            utils.handleError(error, 'فشل في حذف الموعد');
        }
    },

    /**
     * Get CSRF token from cookie
     */
    getCsrfToken() {
        const name = 'csrftoken';
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    },

    /**
     * Show notification
     */
    showNotification(message, type = 'info') {
        // You can replace this with a better UI notification library
        const notification = document.createElement('div');
        notification.className = `alert alert-${type === 'success' ? 'success' : 'info'} position-fixed`;
        notification.style.cssText = 'top: 20px; left: 20px; z-index: 9999; padding: 1rem 1.5rem; border-radius: 0.5rem;';
        notification.textContent = message;
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }
};

// Dashboard Application
const dashboardApp = {
    /**
     * Initialize the dashboard
     */
    init() {
        this.loadAppointments();
        this.setupEventListeners();
        this.updateStats();
    },

    /**
     * Load and display appointments
     */
    async loadAppointments(searchQuery = '') {
        utils.showLoading('api-body');
        
        const appointments = await appointmentManager.fetchAppointments(searchQuery);
        this.renderAppointments(appointments);
        this.updateStats(appointments.length);
    },

    /**
     * Render appointments table
     */
    renderAppointments(appointments) {
        const tbody = document.getElementById('api-body');
        if (!tbody) return;

        if (appointments.length === 0) {
            tbody.innerHTML = `
                <tr>
                    <td colspan="5" class="text-center py-4 text-secondary">
                        لا توجد مواعيد ${document.getElementById('searchInput')?.value ? 'للبحث المطلوب' : ''}
                    </td>
                </tr>
            `;
            return;
        }

        tbody.innerHTML = appointments.map(app => `
            <tr class="fade-in">
                <td class="fw-bold">${app.patient_detail?.user?.username || 'غير معروف'}</td>
                <td>د. ${app.doctor_detail?.user?.username || 'غير معروف'}</td>
                <td>${utils.formatDate(app.date)} | ${utils.formatTime(app.time)}</td>
                <td>${utils.getStatusBadge(app.status)}</td>
                <td>
                    <button class="action-btn" onclick="appointmentManager.deleteAppointment(${app.id})" title="حذف الموعد">
                        <i class="bi bi-trash3"></i>
                    </button>
                </td>
            </tr>
        `).join('');
    },

    /**
     * Update statistics
     */
    updateStats(count = 0) {
        const countElement = document.getElementById('count');
        if (countElement) {
            // Animate the number
            this.animateNumber(countElement, parseInt(countElement.innerText) || 0, count);
        }
    },

    /**
     * Animate number change
     */
    animateNumber(element, start, end) {
        const duration = 500;
        const startTime = performance.now();
        
        const updateNumber = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            
            // Easing function
            const easeOutQuart = 1 - Math.pow(1 - progress, 4);
            const current = Math.round(start + (end - start) * easeOutQuart);
            
            element.innerText = current;
            
            if (progress < 1) {
                requestAnimationFrame(updateNumber);
            }
        };
        
        requestAnimationFrame(updateNumber);
    },

    /**
     * Setup event listeners
     */
    setupEventListeners() {
        // Search input with debounce
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            let debounceTimer;
            searchInput.addEventListener('keyup', (e) => {
                clearTimeout(debounceTimer);
                debounceTimer = setTimeout(() => {
                    this.loadAppointments(e.target.value);
                }, 300);
            });
        }

        // Mobile menu toggle
        const menuToggle = document.getElementById('menuToggle');
        if (menuToggle) {
            menuToggle.addEventListener('click', () => {
                document.querySelector('.sidebar').classList.toggle('active');
            });
        }
    }
};

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    // Initialize dashboard if on dashboard page
    if (document.getElementById('api-body')) {
        dashboardApp.init();
    }
});

// Export for global access
window.appointmentManager = appointmentManager;
window.dashboardApp = dashboardApp;
window.utils = utils;
