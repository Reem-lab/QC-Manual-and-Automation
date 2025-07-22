## Test plan -- objectives:

1- Check main features
Make sure the user can add a task edit it mark it as completed and delete it without any problems

2- Test different types of input
Try entering an empty task special characters and very long text to see how the app reacts

3- Check the design and layout
Look at the page layout and button positions
Make sure everything looks good and works well on all screen sizes

4- Make sure tasks are saved
If the app should save tasks after refreshing the page check that the data is still there

5- Test error messages and feedback
Check that the app shows a message or clear feedback when the user does something wrong like adding an empty task

6- Check if the app is easy to use
Make sure the app is simple to understand and use
Test it using the keyboard and check if labels and tooltips help the user


## Test plan -- scope: 

Checking the main user action: 

- Adding tasks

- Viewing tasks

- Marking tasks as completed

- Deleting a task

--------------------------------------------------------------------------------------------------------------

A [bug report template](https://docs.google.com/spreadsheets/d/1PUR7lzE0O6wXOml7V2Kpl07oylX1K8hmaMT3U3t3A3I/edit?usp=sharing) and 2-3 example bugs based on assumed issues.


## Test cases -- Functional testing:

| Test Case ID | Description            | Steps                                    | Expected Result                                                           |
| ------------ | ---------------------- | ---------------------------------------- | ------------------------------------------------------------------------- |
| TC1          | Add a new to-do item   | Open app → add a new task → Click Add a task button     | Task added in the list                                                  |
| TC2          | Mark item as completed | Click checkbox next to a task            | Task appears as completed by making a line in the middle of the task text |
| TC3          | Delete a task          | Click Delete or Trash icon beside task | Task is removed from the list                                             |


## UI testing

| Test Case ID | Description                  | Steps                            | Expected Result                                   |
| ------------ | ---------------------------- | -------------------------------- | ------------------------------------------------- |
| TC1          | Verify input field alignment | Open app                         | Input field should be centered and aligned        |
| TC2          | Responsive layout check      | Open app on desktop and mobile   | Layout adjusts properly on different screen sizes |



## Boundary Testing

| Test Case ID | Description                   | Steps                                            | Expected Result                                   |
| ------------ | ----------------------------- | ------------------------------------------------ | ------------------------------------------------- |
| TC1          | Add empty task                | Leave input blank → Click Add task               | App shows validation error or disables the button |
| TC2          | Add task with 255 characters  | Enter long string (255 characters) → Click Add task | Task is added successfully                        |
| TC3          | Add task with 256+ characters | Enter 256 characters → Click Add task               | App should restrict or truncate input             |

