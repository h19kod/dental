# Makefile for Dental Clinic System

.PHONY: install migrate run createsuperuser collectstatic test clean shell

# Install dependencies
install:
	pip install -r requirements.txt

# Run migrations
migrate:
	python dental_clinic_system/manage.py migrate

# Create superuser
createsuperuser:
	python dental_clinic_system/manage.py createsuperuser

# Run development server
run:
	python dental_clinic_system/manage.py runserver

# Collect static files
collectstatic:
	python dental_clinic_system/manage.py collectstatic --noinput

# Run tests
test:
	python dental_clinic_system/manage.py test

# Open Django shell
shell:
	python dental_clinic_system/manage.py shell

# Clean cache and temp files
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.log" -delete

# Setup development environment
setup: install migrate createsuperuser
	@echo "Setup complete! Run 'make run' to start the server."
