# Devlog - Avancemos 2.0

---

## Week 1

**Project kickoff and initial planning**

- Defined the core idea: a local skill and service exchange platform connecting people in provinces.  
- Decided the project language and data format: Python with JSON for data storage.  
- Planned console-based user interface for simplicity and accessibility.  
- Drafted main menus:  
  - Main menu with options to register, login, view published services, view requested services, go back, and exit.  
  - User menu with options to view published services, publish new services, request services, chatbot suggestions, go back, and exit.  
- Clarified roles:  
  - *Client* = service requester  
  - *Collaborator* = service provider

---

## Week 2

**User registration and service publishing**

- Implemented user registration flow with optional province selection from a fixed list:  
  1. Almería  
  2. Cádiz  
  3. Córdoba  
  4. Granada  
  5. Huelva  
  6. Jaén  
  7. Málaga  
  8. Sevilla  
- Enabled optional registration for users who just want to browse or request services.  
- Designed a fixed category list for publishing services:  
  - Classes and Training (languages, tutoring, music, IT)  
  - Caregiving (children, elderly, companionship)  
  - Household (cleaning, small repairs, gardening, cooking)  
  - Pets (walking, care)  
  - Wellness and Health (massage, yoga, training)  
  - Creativity and Design (photography, graphic design, crafts)  
  - Technology and Repairs (computers, mobiles)  
  - Transport and Moving (small moves)  
  - Entertainment and Leisure (magic shows, storytelling, tour guide)  
  - Others

---

## Week 3

**Chatbot integration and user session improvements**

- Added a chatbot feature to suggest service categories and personalized service ideas based on user input.  
- Integrated OpenRouter API for chatbot responses.  
- Improved UI to always display the logged-in username at the top of the user menu for clarity and personalization.  
- Standardized output format for “Services Published” section:  
  - Service: *user input service name*  
  - Description: *user input description*  
  - User: *username*  
  - Email: *user email*  
  - Province: *user province*

---

## Week 4

**Testing, bug fixing and final polishing**

- Conducted thorough testing of registration, login, service publishing, and requesting workflows.  
- Fixed bugs related to JSON data persistence and user session handling.  
- Enhanced input validation, especially for province selection and category choices.  
- Finalized console UI flows and navigation options for better user experience.  
- Prepared project documentation, including motivation, setup instructions, usage examples, and contribution guide.  
- Delivered a fully functional console-based Avancemos 2.0 platform ready for local skill and service exchange!

---

**Summary:**  
Over four weeks, we built a Python and JSON-based console app allowing local users to share, request, and discover services. The platform supports flexible payment models and integrates an AI chatbot to inspire service offerings — all while keeping interactions simple, accessible, and community-focused.  
