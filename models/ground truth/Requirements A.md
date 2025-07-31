## Log in
- Actors: Line Worker, Quality Inspector,  Production Manager
- Goal: Authorize to the system
- Main Flow:
	1. The user provides their credentials to the system
	2. The system checks the credentials against the user database. Then it authorizes the user or shows an appropriate error message.
## Update Production
- Actors: Line Worker
- Goal: Update their production in the system (why is this needed? the system should monitor it by itself!)
- Main Flow:
	1. The line worker selects "update production"
	2. The system shows an input mask to enter the production
	3. The line worker enters appropriate values and confirms them
	4. The system stores the input and returns the user to the system overview
## Report Malfunction
- Actors: Line Worker
- Goal: Report a malfunctioning machine to the system
- Main Flow:
	1. The line worker selects "report malfunction"
	2. The system asks for the details of the malfunction
	3. The line worker enters appropriate values and confirms them
	4. The system stores the input and returns the user to the system overview
## Report Lack of Material
- Actors: Line Worker
- Goal: Report missing supply materials to the system
- Main Flow:
	1. The line worker selects "report lack of material"
	2. The system asks for the type of missing material and the amount that is still available
	3. The line worker enters appropriate values and confirms them
	4. The system stores the input and returns the user to the system overview
## Inspect Product for Quality
- Actors: Quality Inspector
- Goal: Ensure the machines are working within quality boundaries
- Main Flow:
	1. The quality inspector takes a product sample and checks it against a list of quality criteria
	2. In case the product violates the quality criteria, the quality inspector decides whether to _Stop the Line_, _Mark the Batch for Rework_, or discard only the failed product(s) as a one-off
	3. The quality inspector may repeat the use case for a more thorough assessment
## Stop a Line
- Actors: Quality Inspector
- Goal: Make sure no further faulty goods are manufactured
- Main Flow:
	1. The quality inspector selects "stop a production line"
	2. The system prompts for the production line ID
	3. The quality inspector enters the appropriate value
	4. The system logs the action, shuts the line down gracefully and returns the user to the system overview
## Mark Batch for Rework
- Actors: Quality Inspector
- Goal: Increase the quality of already manufactured goods so they conform to the quality standards
- Main Flow:
	1. The quality inspector selects "mark a batch for rework"
	2. The system prompts for the batch number
	3. The quality inspector enters the appropriate value
	4. The system logs the action, adds the batch to the production schedule again and returns the user to the system overview
## Revise Production Schedule
- Actors: Production Manager
- Goal: Resolve scheduling problems that arose
- Main Flow:
	1. The production manager selects "revise production schedule"
	2. The system prompts for the schedule ID that should be edited
	3. The production manager enters the appropriate value and confirms
	4. The system displays the production schedule and shows an editing interface
	5. The production managers makes changes at will and saves them
	6. The system updates the production schedule, logs the changes and returns to the overview page
## Inspect Reports
- Actors: Production Manager, Quality Inspector
- Goal: Understand potential problems in the production
- Main Flow:
	1. The user selects "show reports"
	2. The system shows an overview of all reports that the user has access to
	3. The user selects one of the shown reports
	4. The system shows all information available on the selected report
	5. The user closes the report and is returned to the report overview
	6. The user closes the report overview and is returned to the system overview