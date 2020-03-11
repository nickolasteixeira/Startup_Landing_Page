# custom-landing page

## Architecture 

Web App will run on AWS EC2 instance and communicate with the [sendy API](https://sendy.co/api)
when a user adds their contact information. Before this can happen, you'll have to provision the 
resources and run the installation scrips below to set up the sendy dashboard. 

### Typical flow:
A user lands on the website and enters their information. That request is sent to `/beta` route
in on the server, which validates the request. If it's valid, another server request is sent to the
sub domain that you installed the sendy app with the sendy API routes. After the requests successfully
completes, a user will get redirected to a completed screen. 

How to:
- Install [Sendy](https://sendy.co/) with these [scripts](./sendy_installation_scripts)


### To dos:
- [x] Create bash script to install sendy for AWS EC2 resources 
- [ ] Create terraform script for Sendy to provision
- [ ] Create terraform script for Backend/Frontend resources for Custom Landing Page
- [ ] Create Front-End React templates for Custom Landing Page
- [ ] Hook up Front-End HTTP form requests to backend routes
- [ ] Hook up backend routes `/beta` to send requests to [sendy API](https://sendy.co/api)

