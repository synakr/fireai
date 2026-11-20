# Research — QR Print Bridge

## 1. Problem Statement

1. Printing shop vendors (Mr Shital Ghosh) often have to manage printing requests while handling other shop responsibilities, making it difficult for them to attend to multiple print jobs at the same time.

2. As they are using whatsapp for most of the task, each print request requires manual work, such as downloading files, identifying the customer, adjusting print settings and preparing the pages. Doing this separately for every order takes time and increases customer waiting times.

3. As a result, customers coming for print jobs, as well as those visiting the shop for other services, often end up waiting in long queues and wasting valuable time.

4. Long waiting times can frustrate customers, and some may eventually leave without getting their work done. This results in loss in both time and potential business for customer and the vendor respectively.

5. Most print requests are often shared through WhatsApp, where handling messages from multiple customers can become confusing. There is also no proper system to organize incoming orders or keep track of previous requests, causing messages and files to pile up.

## 2. Existing Solutions

### Solution 1: Self-Service Printing ATMs — QwikPrint

Website: https://www.qwikprint.in/

Reference: [The Better India — Stuck In A 45-Minute Xerox Queue, Two Chennai Friends Built a Printing ATM](https://thebetterindia.com/startup/self-service-printing-kiosks-qwikprint-startup-chennai-india-12659397)

QwikPrint offers self-service printing kiosks that allow customers to scan a QR code, upload documents, select printing preferences, make digital payments, and collect printouts through an OTP-based system.

**Why it may not fit the intended vendor:**

- The solution relies on dedicated kiosk hardware and infrastructure rather than utilizing the vendor's existing computer and printer setup.
- Small printing businesses that have already invested in conventional printing equipment may find it impractical to replace or abandon their existing infrastructure.
- Procuring, installing, and maintaining dedicated self-service kiosks introduces additional investment and operational requirements that may not be suitable for smaller vendors, as he wont be able ro afford it after already doing so much investment on the current machines.

**Our approach:** QR Print Bridge aims to bring similar self-service automation to existing print shops without requiring dedicated kiosk hardware. It utilizes the vendor's existing computer and printer infrastructure, introducing a software-based bridge for customer document submission, print configuration, and centralized job management while allowing vendors to retain control over the printing process.

### Solution 2: Manual WhatsApp Intervention

The existing WhatsApp-based approach works, but it involves considerable manual effort and repetitive tasks, resulting in delays and operational confusion.

- **Time-consuming workflow:** Every print request requires the vendor to manually download files, identify customer requirements, configure print settings, and process the job.
- **Lack of file management:** WhatsApp does not provide a dedicated print-job management system. The vendor must manually manage downloaded files, organize them, and clean up storage after completing print jobs.
- **Repeated configuration requests:** Customers often need to communicate their printing preferences repeatedly. This can lead to misunderstandings, frustration, and printing errors, such as incorrect page ranges or inconsistent colour and layout settings.
- **Limited workflow visibility:** Customers have little visibility into their job status or waiting time, often requiring them to follow up with the vendor manually.

**Our Approach:**

QR Print Bridge aims to introduce self-service automation into existing print shops without requiring manual intervention from the shopkeeper for every request.

Customers simply scan a QR code, upload their documents, configure their printing preferences, and submit their jobs directly. They can also track their position in the print queue and estimated waiting time, improving transparency and helping them manage their time more effectively.

## 3. Sources Read

### Source 1: The Better India — QwikPrint Printing ATMs

https://thebetterindia.com/startup/self-service-printing-kiosks-qwikprint-startup-chennai-india-12659397

- Describes how QwikPrint addresses long queues at conventional printing shops through self-service printing kiosks.
- Explains its QR-based document upload, print configuration, digital payment, and OTP-based collection workflow.
- Helped establish the printing ATM model as an existing approach and identify the possibility of bringing similar automation to conventional printing shops without dedicated kiosk hardware.

### Source 2: WhatsApp Management Issues

[The Disadvantages of Using WhatsApp for Business Purposes – Teamwire](https://teamwire.eu/en/blog/the-disadvantages-of-using-whatsapp-for-business-purposes/)

The article highlights several limitations of using WhatsApp for business communication:

- **Contact-saving requirements:** Depending on the communication method and business account setup, customers may need to save or otherwise establish the business contact before initiating communication and sharing files.
- **Onboarding friction:** Requiring customers to interact through WhatsApp and follow additional steps can make the initial experience less seamless.
- **Personal number dependency:** WhatsApp accounts are typically associated with phone numbers. This can be convenient for direct communication but may also create privacy and separation concerns when vendors use personal numbers for business operations.

These limitations further highlight the need for a dedicated, self-service print submission and job management system.
