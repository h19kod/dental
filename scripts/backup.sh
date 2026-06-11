#!/bin/bash
# Backup script for Dental Clinic System

BACKUP_DIR="backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
DB_FILE="dental_clinic_system/db.sqlite3"
MEDIA_DIR="dental_clinic_system/media"

echo "🦷 Creating backup..."

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup database
if [ -f "$DB_FILE" ]; then
    echo "📦 Backing up database..."
    cp "$DB_FILE" "$BACKUP_DIR/db_$TIMESTAMP.sqlite3"
fi

# Backup media files
if [ -d "$MEDIA_DIR" ]; then
    echo "📁 Backing up media files..."
    tar -czf "$BACKUP_DIR/media_$TIMESTAMP.tar.gz" -C dental_clinic_system media
fi

echo "✅ Backup complete: $BACKUP_DIR"
ls -lh $BACKUP_DIR/
