# 1. Create project folder
# 2. Right click it, select Git Bash Here
# 3. To create a file in the folder, use $ touch <file_name.extension>
# 4. $ git init to initialise the .git folder
# 5. Add name and email to the git configuration using $ git config --global user.name 'Alix Decrop'
# and $ git config --global user.email 'alix.decr@gmail.com'
# 6. To add file in the .git folder, use $ git add <file_name.extension>
# 7. To remove file from the .git folder, use $ git rm --cached <file_name.extension>
# 8. To add all project files, use $ git add .
# 9. Use $ git status to see the status of .git
# 10. Use $ git commit to commit -> a vim editor will open, type i to enter insert mode, remove # for comment then exit insert mode using escape and now type in :wq then enter TO SKIP THIS STEP : $ git commit -m '<comment>'
# 11. $ touch .gitignore to create a folder where ignored files will be (logs for example, ignored in $ git add .)
# 12. To ignore a file, just add <file_name.extension> in the .gitignore file ; use /<folder_name> to add a folder ; *.<extension> to ignore all files of the given extension
# 13. To create a branch, use $ git branch <branch_name> (to work on a different branch than the master one)
# 14. $ git checkout <branch_name> to switch to another branch ; If we update in a branch, it will not appear in other branches (especially master)
# 15. $ git merge <branch_name> to add updated files from a branch to the master branch (merge the branches?)
# 16. To add onto GitHub, use $ git remote add origin <github_repo_url> with origin = <name>
# 17. To push onto GitHub, use $ git push -u origin <branch_name>

def testFunction():
    print('Hello Git!')
    print('Updated...')

testFunction()
