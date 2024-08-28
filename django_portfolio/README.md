
# Django Portfolio Website
## Overview
This is a **basic portfolio website** built using Django, a powerful Python web framework. The website is styled with Materialize, a modern responsive front-end framework based on Material Design principles. This static site showcases your work and provides information about your skills and projects.

## Features

 - **Responsive Design:**  The site is fully responsive, ensuring a great user experience on all devices.
 - **Modern Styling:** The website uses Materialize for a clean, modern look.
 - **Static Content:** The website does not require a database, as it only serves static content.


## Usage

- **Templates:** Customize the HTML templates located in the **`templates`** directory to personalize your portfolio content.
- **Static Files:** All CSS, JavaScript, and images are stored in the **`static`** directory. Modify these files to change the styling or add new content.
- **Materialize:**  The site is styled using Materialize. Refer to the [Materialize Documentation](https://materializecss.com/) for additional styling options.

## Deployment

To deploy the website on a live server:

- **Collect Static Files:**
```bash
  python manage.py collectstatic
```

- **Configure the Server:** Follow the standard Django deployment steps using a WSGI server like Gunicorn, and set up a web server like Nginx or Apache.

- **Update Allowed Hosts:** Ensure that your domain name is added to the ALLOWED_HOSTS list in your Django settings.

## License

This project is licensed under the MIT License - see the LICENSE file for details. [MIT](https://choosealicense.com/licenses/mit/)


## Feedback

For feedback, issues, or suggestions, please contact https://github.com/moizazfar

