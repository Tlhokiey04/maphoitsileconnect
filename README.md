@@ -0,0 +1,169 @@
# MaphoitsileConnect 🌍

## Community Service Delivery System
A web-based platform that allows community members to report and track 
service delivery issues such as water leaks, electricity faults, 
potholes, and waste collection problems.

Built for **NHCI63110 – Human-Computer Interaction Assignment**  
Sol Plaatje University | Student: Tlhokomelo Matsitle | 202407083

---

## 🚀 Features

- ✅ User Registration and Login
- ✅ Report service delivery issues (Water Leak, Pothole, Electricity, Waste)
- ✅ Upload photos as evidence
- ✅ Track issue status (Pending → In Progress → Resolved)
- ✅ Personalised dashboard with stat cards
- ✅ Filter reports by status
- ✅ Unique reference number for each report
- ✅ Admin panel to manage and update issues
- ✅ Responsive design (works on mobile and desktop)
- ✅ Status timeline on each issue

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.14 | Backend programming language |
| Django 5.x | Web framework |
| SQLite | Database |
| Bootstrap 5 | Frontend styling |
| Bootstrap Icons | UI icons |
| Pillow | Image upload handling |
| Git & GitHub | Version control |

---



## 📱 Pages and URLs

| Page | URL |
|------|-----|
| Login | http://127.0.0.1:8000/ |
| Register | http://127.0.0.1:8000/register/ |
| Dashboard | http://127.0.0.1:8000/accounts/dashboard/ |
| Report Issue | http://127.0.0.1:8000/reports/new/ |
| My Reports | http://127.0.0.1:8000/reports/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

---



## 🎨 Design Principles Applied

- **Visibility** — 3-step progress indicator on report form
- **Feedback** — Confirmation page with reference number after submission
- **Consistency** — Same navbar, badges, and layout across all pages
- **Affordance** — Clear buttons and labels guide users naturally
- **Inclusiveness** — Colour + text labels support colour-blind users

---

## 📂 Project Structure
```
maphoitsileconnect/
  app/
    templates/
      reports/
        base.html
        report_form.html
        success.html
        issue_list.html
        issue_detail.html
      accounts/
        login.html
        register.html
        dashboard.html
    models.py
    views.py
    forms.py
    admin.py
  maphoitsile/
    settings.py
    urls.py
  manage.py
  README.md
```

---

## 🔑 Admin Access

To update issue statuses (Pending → In Progress → Resolved):
1. Go to http://127.0.0.1:8000/admin/
2. Login with your superuser credentials
3. Click on **Issues**
4. Change the status of any issue directly from the list

---

## 📸 Screenshots

> Register page, Dashboard, Report Form, Success Page, 
> Issue Detail with Timeline — add screenshots here

---

## 📜 License

This project was developed for academic purposes at Sol Plaatje University.  
NHCI63110 — Human-Computer Interaction | 2026
