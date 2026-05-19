# D & L Water Solutions Uganda Limited — Django Website

## Setup Instructions

### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run migrations
```bash
python manage.py migrate
```

### 4. Create an admin user (optional)
```bash
python manage.py createsuperuser
```

### 5. Run the development server
```bash
python manage.py runserver
```

### 6. Open your browser
Visit: http://127.0.0.1:8000

---

## Pages

| URL | Page |
|-----|------|
| / | Home |
| /products/ | Products & Features |
| /about/ | About Us |
| /contact/ | Contact Form |
| /admin/ | Admin Dashboard |

## Features
- Responsive design (mobile-friendly)
- Contact form with database storage
- Admin panel to view all enquiries
- UV purifier product showcase
- Google Fonts (Sora + DM Sans)
- Smooth scroll animations

## Customisation
- Update `dlwater/settings.py` with your production SECRET_KEY
- Set `DEBUG = False` for production
- Configure email backend in settings.py to receive real contact form emails
