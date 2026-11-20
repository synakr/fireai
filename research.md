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

- Current whatsapp method works, but its lot of time sonsuming as well as repeated works are there, leading to confusion
- There is no proper memory management in whatsapp; Vendor has to do all the memory management by himself; he have to cleanup spaces himself after downloading the files and doing the printing jobs;
- Repeated asking of printing configuaration often lead to confusion and frustration; this often leads to mistakes; like page number may very; color cofiguration might vary.

**Our approach:** QR Print Bridge aims to bring similar self-service automation for existing print shops without intervention from the shopkeeper. The user scans the qr, inputs the config and gets the printing job done directly; he see his queue and waiting time, hence time management can be done well

## 3. Sources Read

### Source 1: The Better India — QwikPrint Printing ATMs

https://thebetterindia.com/startup/self-service-printing-kiosks-qwikprint-startup-chennai-india-12659397

- Describes how QwikPrint addresses long queues at conventional printing shops through self-service printing kiosks.
- Explains its QR-based document upload, print configuration, digital payment, and OTP-based collection workflow.
- Helped establish the printing ATM model as an existing approach and identify the possibility of bringing similar automation to conventional printing shops without dedicated kiosk hardware.

### Source 2: WhatsApp Management issues

https://teamwire.eu/en/blog/the-disadvantages-of-using-whatsapp-for-business-purposes/

- Describes how the new user needs to manually save the contact first in order to send files because of whatsapp business policies.
- Onboarding might be messy for the vendor
- Accounts are linked to personal phone numbers; might have both advantage as well as disadvantage
