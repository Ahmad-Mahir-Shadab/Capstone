#  Capstone

This was CS50W

## Distinctiveness:
I made a **Notes** app using Django. I use notes often when I'm learning, so I thought it would be a great idea to make a Notes app. In this app, I have implemented **several** real-life features used in a notes app. This app contains only 1 Django model and utilizes JavaScript. I have used Bootstrap 5. This project aims to create a notes app that anyone can use and create a project that the CS50 staff will deem distinct enough from other projects. The aesthetics is also vastly different from all other projects.

## Complexity:
I believe this project is an intermediate type of difficulty. Even though a notes app is generally a beginner-level project. I have created **8** features which should make this project count as intermediate lever difficulty. Features:
1. Create a New Note
2. Index Page
3. Creating a new page for every note
4. Search
5. Pagination
6. Editing Note using JavaScript
7. Deleting a Note
8. Mobile Responsiveness

## Create new note:
On the homepage of the project, there's a link named "Create New Note". Upon clicking it, the user is presented with a form a title, and details of that note. Clicking on the submit button, the user is redirected to the newly created note.

## Index Page:
On the index page/homepage, all of the notes are shown. Clicking on a note's title redirects the user to the page dedicated to the clicked note.

##  Creating a new page for every note:
For every note shown, there is a whole new page created dedicated to every note. To access it, the user has to click on the note's title. There, they will be able to see the note more clearly as I say. Equipped with the edit and delete buttons.

## Search:
There's a form on the homepage. It is used for searching for any particular note. If a part of the note(s)'s title is typed, the form will show all of the notes that match the queried data with the note(s) title; that is if, any note exist
with the queried data.

## Pagination:
On the homepage, only 4 notes are shown at a time. If there are more than 4 notes, you will be able to see the 5th note 2nd page and so on and so forth. The most recent notes shown are at the top.

## Editing Note using JavaScript:
This feature is inspired by Project 4. There's a button named "Edit" for every note. This button can be found on the index and the dedicated(to note) page. Upon clicking, a modal appears with the note's description pre-existing. After editing the note's description, the user must click on the "Save Changes" button. That button closes the modal and replaces the note's description with the user's newly written description instead of the old one.

## Deleting a Note:
There's a button named "Delete" for every note. This button is red-coloured. This button can be found on the index and the dedicated(to note) page. Any note will be deleted upon clicking on this button.

## Mobile Responsiveness:
This one is pretty self-explanatory. This project can be viewed from a mobile device and the project looks good!

### How to run Notes:

Final Project of [CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/)
A Notes app!
[Full project specification](https://cs50.harvard.edu/web/2020/projects/4/network/)

<img src="graphics/Screenshot 2024-05-03 122106.png" width=500>

#### Setup
First, clone the repository.
```bash
git clone https://github.com/me50/Ahmad-Mahir-Shadab/tree/web50/projects/2020/x/capstone
cd capstone
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Django requires a secret key, so you will need to make sure that you add one to your *bash profile*.

```bash
SECRET_KEY="your-secret-key-goes-here"
export SECRET_KEY 
```

You can generate a random secret key by running:

```bash
python -c "import secrets; print(secrets.token_urlsafe())"
```


To run the development server:
```bash
python manage.py runserver
```

## Visuals:
Click [here](https://youtu.be/FLnkO7-iZjo) to see the project in action.