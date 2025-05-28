# Project 1 - Static Website Deployment Using GCP

This guide walks you through deploying a static website on Google Cloud Platform (GCP) using Cloud Storage and Cloud CDN for a scalable, cost-effective, and high-performance hosting solution. 

## Table of Contents

1. [Steps](#Steps)
2. [Creating Google Storage Bucket](#creating-google-storage-bucket)
3. [Common Error Corrections](#common-error-corrections)

## Steps

1. Create an `index.html` File.
2. Open GCP and login in with your account.
3. Browse and find Compute Engine and click on it.
4. Browse to VM insntances. (On your left, click on Virtual Machine to find it)
5. Click on the Create Instance button. 

![image1](./read_me_images/step%201.jpg)

6. Navigate to Machine Configuration on the left panel.
7. Name your Instance. (In the above image `project1`)
8. Select `us-west1 (Oregon)` in Region, and `us-west1-b` in Zone, in order to decrease your monthly estimate.
9. In the general purpose section, select the E2 in the Series.

![image2](./read_me_images/step%202.jpg)

10. Scroll down in the same window and find `Machine Type`
11. Select `Preset` and select `e2-micro (2 vCPU, 1 core, 1GB memory)` from the dropdown.
12. Navigate to OS and Storage in the left Panel.
13. In the Operating System options, click on Change.

![image3](./read_me_images/step%203.jpg)

14. Select Ubuntu in `Operating System` dropdown.
15. Select Ubuntu 20.04 LTS in the `Version` dropdown.
16. Select Standard persistent disk in the `Boot disk type`.
17. Select 10 GB in the `Size(GB)` dropdown.
18. And then click on the `Select` button.

![image4](./read_me_images/step%204.jpg)

19. Navigate to `Networking` in the left panel.
20. In the `Networking` section in the middle, Check the options: 
    `Allow HTTP traffic` and `Allow HTTPS traffic`
21. Click on the `Create` button.

![image5](./read_me_images/step%205.png)
This will create your instance.
    
22. In your instance, Click on the `SSH` in the connect column at the right most.
23. A new terminal window with the title `SSH-in-browser` will popup.
24. Enter the following commands in the terminal:

``` 
sudo su 
```
This will show the `root@\<your instance name>`, then: 

![image6](./read_me_images/step%206.jpg)

```
cd
```

This will show your root project, type in :

```
apt-get install apache2
```

Type in `'Y'` when prompted if you want to continue.

![image7](./read_me_images/step%207.jpg)

Then type in :

```
service apache2 status
```
![image8](./read_me_images/step%208.jpg)

To check if the service is active and running or not.

Then copy the External IP from your instance in the GCP website.

25. Paste the copied IP in the browser with "http://\<your external ip>"

If the website loads correctly, a default page will description will show up.

![image9](./read_me_images/step%209.png)

26. Now go back to your GCP website and to your instance. 

27. Click on `SSH` to open a new terminal.

28. Follow the commands to Install Google Cloud in our Virtual Machine:

```
sudo apt-get install -y google-cloud-sdk
```

Then :

```
gcloud auth login
```

Your terminal should look like this: 

![image10](./read_me_images/step%2010.jpg)

Type in 'Y' when you are prompted to continue.

Copy the link that will be generated and paste it in your browser.

![image11](./read_me_images/step%2011.jpg)

Copy the code and paste it back into the same SSH terminal.

Your tab should look like this:

![image12](./read_me_images/step%2012.png)

This will create the Google Clound in your machine.

Now follow the steps below to make a Bucket in the Google Cloud Storage:

#### Creating Google Storage Bucket

1. Go to Google Cloud Website and click on `Create a Storage Bucket`

2. Then Type in your bucket's name and scroll down to find the `Create` button and click on it.

3. Upload your index.html and other files in the upload section.

<a name="OpenSSH"></a>

4. Open the SSH terminal from your instance.

Type in the command: 

```
gsutil cp gs://'your-bucket-name'/'your-folder-name'/index.html /var/www/html/index.html
```

Your terminal should have the command entered like this: 

![image13](./read_me_images/step%2013.png)

5. Come back to the browser tab that has the \<External IP> and reload it.

![image14](./read_me_images/step%2014.jpg)

If the website loads with your html file, your website has successfully hosted.

![image15](./read_me_images/step%2015.jpg)

## Common Error Corrections

### If No URLs Found:

Type in this command in the SSH terminal from your instance to find the path of the project:

```
gsutil ls -r gs://'your-bucket-name'/
```

This will show your path.

Repeat the steps from Step `4` from the [Create Bucket Sections](#creating-google-storage-bucket).


### If Permission is Denied

Type in the follow command into the SSH Terminal from your instance in the GCP website:

```
gsutil cp gs://'your-bucket-name'/'your-folder-name'/index.html /var/www/html/index.html
```

Then enter these two commands into the terminal:

```
sudo chown -R $USER:$USER /var/www/html/
sudo chmod -R 755 /var/www/html/
```

Repeat the steps from Step `4` from the [Create Bucket Sections](#creating-google-storage-bucket).


# Project 3 - Cloud Storage and Data Management

This Guide will help you create Cloud Storage Bucket and perform data backup, versioning, and cloud storage for serving data step by step.

## Steps

#### Creating Google Storage Bucket

1. Go to Google Cloud Website and click on `Create a Storage Bucket`

2. Then Type in your bucket's name and scroll down to find the `Create` button and click on it.

3. Upload your index.html and other files in the upload section.

Your tab should look like this:

![image12](./read_me_images/step%2013.png)

<a name="OpenSSH"></a>

4. Open the SSH terminal from your instance.

5. This is to Enable object versioning in your GCP bucket.

Object versioning helps keep multiple versions of a file, so if something is deleted or overwritten, you can restore it.

Type in the command: 


```
gsutil versioning set on gs://'your-bucket-name'
```

6. Check if versioning is happening.

Type in the command: 

```
Object versioning helps keep multiple versions of a file, so if something is deleted or overwritten, you can restore it.
```
7. It Should return True

8. Backup Data to Cloud Storage

To back up files from your VM to your bucket, use:

```
gsutil cp -r /var/www/html/ gs://'your-bucket-name'/website-backup/
```
This copies your entire website files to Cloud Storage.
If you want to schedule backups, use a cron job:

9. Setup automatic backups (cron job)

Type in the command:
```
crontab -e
```
This opens the crontab.

10. Select an Editor

Type 1 and press Enter to use Nano (it's the easiest).
This will open an empty crontab file for scheduling tasks.

![image16](./read_me_images/step%2016.jpg)

11. Add Your Backup Job

Now that crontab is open, scroll down and add this line at the bottom:

Type in the command:
```
0 2 * * * gsutil -m cp -r /var/www/html/ gs://your-bucket-name/website-backup/
```

What this does:

Runs the backup every day at 2 AM
, -m enables parallel processing for faster uploads, 
Adjust the timing if needed `(0 2 * * * means 2 AM daily)`.

![image17](./read_me_images/step%2017.jpg)

12. Save and Exit

Press `CTRL + X` to exit
Press `Y` (for Yes) and then Enter to `save the file`.

13. Verify Crontab is Set
Run:

Type in the command:
```
crontab -l
```
If you see your backup command, it means cron is now scheduled 

14.  Test the Backup Manually
To make sure it works, run the backup command immediately:

```
gsutil -m cp -r /var/www/html/ gs://your-bucket-name/website-backup/
```
If it uploads the files successfully, cron will work at the scheduled time.

The Final SSH commands would like this:

![image18](./read_me_images/step%2018.jpg)

Now the website is backed up and automated as well.






