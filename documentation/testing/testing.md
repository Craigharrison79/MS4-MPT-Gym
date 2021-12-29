# Issue

## Dropdown menu not working

The mobile dropdown navbar was not working.  After looking through the code, I noticed I was missing BS in the data-bs-toggle="dropdown". 

## Webhooks not working

Trying to setup the webhook for the checkout and payment. I was following the boutique_ado video but after a few attempt the test was not passing. Getting a 401 error!

![webhooks](/documentation/testing/files/webhooks/test-webhook-attempt.png)
![webhooks](/documentation/testing/files/webhooks/failing-webhook-test.png)

I check over my secret keys and sign in key:

![webhooks](/documentation/testing/files/webhooks/stripe-key.png)

I started looking on StackOverflow and on slack. I read on slack some students were having the same problem and once you shared on Gitpod the issue would go away. I check and I was not sharing my Gitpod.  Once I Shared the issue disappear and I got 200 code.

![webhooks](/documentation/testing/files/webhooks/not-shared.png)
![webhooks](/documentation/testing/files/webhooks/shared.png)

## Migration Issue to Postgres

On migrating my models over to Postgres for deployment to Heroku I was getting an issue with Club and Product Id this was due to the fact I started the project using UUID and then change back to primary_key as I was having issues getting the checkout function working due to my lack of knowledge with Database.  This was a big decision as I couldn't get postgres to migrate.  The Code Institute Tutor help me through the issue.

![migrations-club](/documentation/testing/files/postgres-migration/club-migrate.png)
![migrations-product](/documentation/testing/files/postgres-migration/product-migrate.png)
![migrations-issue](/documentation/testing/files/postgres-migration/showmigration-issue.png)

I had to delete the migrations files except for the __init__.py on club and product. Then resetting the Postgres in Heroku by first going to Heroku resources tag:

![migrations-resources](/documentation/testing/files/postgres-migration/heroku-resources.png)

Then click on the Heroku Postgres icon and then press reset database.

![migrations-reset](/documentation/testing/files/postgres-migration/reset-db-heroku.png)

Once this was done in Gitpod check showmigrations was clear:

![migrations-clear](/documentation/testing/files/postgres-migration/showmigration-clear.png)

Then makemigrations and migrate again.

![migrations-migrate](/documentation/testing/files/postgres-migration/migrate.png)

## Split bewteen Gidpod and GitHub

This was a big issue and I couldn't fix this issue, one of the tutors at Code Institute fixed it for me.

![CI-tutor](/documentation/testing/files/issue-with-github/tutor.png)

This issue took roundabout 4 hours to fix. From what the tutor explain Gitpod and Github had split and my commits were not committing to Github.  

![Github-issue](/documentation/testing/files/issue-with-github/github-issue.png)

Sean tries pulling the code from GitHub:

![git-pull](/documentation/testing/files/issue-with-github/git-pull.png)

He got some of the issues fixed but the db.sqlite3 was being a  problem so we talked, about me losing the database and  I was ok with it as I just had a few items in the database for testing. So wouldn't be a big loss or a hard thing to redo. Still feel it was because of the Postgres issue from above.  I don't know everything he tried as he was working on a for a while and also had to ask other people for help.  

He ended up branching out the mainline stopping merge, pushing upstream, and force push to Github.  I didn't fully get it.  But here is his explanation:

![tutor-explain](/documentation/testing/files/issue-with-github/tutor-explain.png)

Here is a lot of code, that I took a screenshot of as he was working on the issue.

![issue](/documentation/testing/files/issue-with-github/some-code.png)
![issue2](/documentation/testing/files/issue-with-github/some-code-2.png)
![issue3](/documentation/testing/files/issue-with-github/some-code-3.png)
![issue4](/documentation/testing/files/issue-with-github/some-code-4.png)
![issue5](/documentation/testing/files/issue-with-github/some-code-5.png)
![issue6](/documentation/testing/files/issue-with-github/some-code-6.png)
![issue7](/documentation/testing/files/issue-with-github/some-code-7.png)
![issue8](/documentation/testing/files/issue-with-github/some-code-8.png)
![issue9](/documentation/testing/files/issue-with-github/some-code-9.png)
![issue10](/documentation/testing/files/issue-with-github/some-code-10.png)


## Issue Gitpod Update and add requirements.txt when freezing.

When I was setting up Heroku deployment and freeze requirements to check everything was saved in my files, Gitpod was adding extra things. I should have had 21 packages listed but I had 125 packages listed in the file.  On calling Code Institute Tutor they inform me that this was an issue because of a change or update to Gitpod.

I had to close the workspace I was using and open up a new one.  
![workspace](/documentation/testing/files/heroku/new-workspace.png)

Before closing the workspace down I had to clean out the requirements.txt file and save it.  Add/commit and push to GitHub.
 
![fix-issue](/documentation/testing/files/heroku/fix-issue.png)

I had to close the workspace I was using and open up a new one.  
![workspace2](/documentation/testing/files/heroku/workspace.png)

In Github open up the repository and hit Green Gitpod button and build a workspace.

In the new workout I had to pip3 install -r requirements.txt and then I could deploy to heroku.