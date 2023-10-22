# Screenshot Upload and GitHub Push Guide

This guide will walk you through the process of taking screenshots of completed levels, transferring them to a sandbox environment using SFTP, and then pushing the screenshots to GitHub. 

## Prerequisites

- Access to the sandbox environment (You will need the hostname, username, and password provided to you for the sandbox environment).
- A terminal or command prompt on your local machine.

## Step 1: Take Screenshots

Take screenshots of the completed levels as mentioned in the general requirements.

## Step 2: Open Terminal

Open a terminal or command prompt on your local machine.

## Step 3: Connect to Sandbox Environment

Use the SFTP command-line tool to establish a connection to the sandbox environment. Replace `<hostname>`, `<username>`, and `<password>` with the provided information.

```bash
sftp <username>@<hostname>
```

## Step 4: Navigate to Destination Directory

Once connected, navigate to the directory in the sandbox environment where you want to upload the screenshots.

```bash
cd /path/to/destination/directory
```

## Step 5: Upload Screenshots

Use the SFTP put command to upload the screenshots from your local machine to the sandbox environment. Replace <local_path> with the actual path to your screenshots on your local machine.

```bash
put <local_path>
```

## Step 6: Confirm Transfer

Confirm that the screenshots have been successfully transferred by checking the sandbox directory.

## Step 7: Push to GitHub

Once the screenshots are transferred to the sandbox environment, you can proceed to push the screenshots to GitHub as mentioned in the initial requirements.

That's it! You've successfully uploaded your screenshots to the sandbox environment and pushed them to GitHub.