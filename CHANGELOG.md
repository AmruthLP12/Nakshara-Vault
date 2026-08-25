# Changelog

## Versioning Guide (Keep It Simple)

Use this pattern:

MAJOR.MINOR.PATCH

### When to Change What:

- **MAJOR (1 → 2)**  
  Big changes / breaking changes  
  (e.g., redesign, major module rewrite)

- **MINOR (1.2 → 1.3)**  
  New features added  
  (most of your daily work will be this)

- **PATCH (1.3.0 → 1.3.1)**  
  Bug fixes / small tweaks

---

All notable changes to this project will be documented in this file.

# Run **clog** to generate the changelog with today's date

---

## [0.1.0] - 2026-08-25

### Added

- Created the new **Digital Asset Management (DAM) / Image Gallery** project named **DAM**.
- Initialized the Django project using:
  - `uv init .`
  - `uv add django`
  - `uv run django-admin startproject core .`
  - `uv run python manage.py startapp gallery`

- Created `CHANGELOG.md` to track project changes.
- Created `Makefile` to define common development commands.

#### Gallery App

- Created the `Image` model in `gallery/models.py`.
- Added the following fields to the `Image` model:
  - `title`
  - `description`
  - `image`
  - `uploaded_by`
  - `is_public`
  - `created_at`
  - `updated_at`

- Configured the `image` field to use private storage through `private_storage`.

#### Project Settings

- Added the `gallery` app to `INSTALLED_APPS`.
- Added static file configuration:
  - `STATIC_URL`
  - `STATIC_ROOT`

- Added media file configuration:
  - `MEDIA_URL`
  - `MEDIA_ROOT`

- Added `PRIVATE_MEDIA_ROOT` for private media storage.

#### URL Configuration

- Added static file URL configuration.
- Added media file URL configuration.
- Included `gallery.urls` in the project's URL configuration.

#### Django Admin

- Created `ImageAdmin` for the `Image` model.
- Added `autocomplete_fields`.
- Added `date_hierarchy`.
- Added `list_display`.
- Added `list_filter`.
- Added `search_fields`.
- Added `readonly_fields`.
- Added custom `fieldsets`.
- Added the `image_preview` method for displaying image previews in the admin.

#### Image File Handling

- Created `gallery/views/image_views.py` to handle image file requests.
- Created `gallery/urls/image_urls.py` to define image-related URLs.
- Created `gallery/urls/__init__.py` to include the image URL configuration.

### Changed

- Updated `image_preview` in `gallery/admin.py` to use `reverse()` for generating the image URL.
- Updated `image_preview` to use `format_html()` for generating the preview HTML.
- Updated `image_preview` to return the image URL when the `image` field is empty.

### Fixed

- None.

### Removed

- Removed the old `gallery/views.py` file after moving image-related views to `gallery/views/image_views.py`.

---
