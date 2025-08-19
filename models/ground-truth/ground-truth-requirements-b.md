## Login
- Actors: Nurse, Doctor
- Goal: Authorize to the system
- Main Flow:
	1. The user provides their credentials to the system
	2. The system checks the credentials against the user database. Then it authorizes the user or shows an appropriate error message.
## Access or Change Patient Record
- Actors: Nurse
- Goal: Get the available information on a patient and update them if needed	
- Main Flow:
	1. The user selects "patient records"
	2. The system shows a list of patient records
	3. The user filters for the patient optionally and then selects them
	4. The system shows all information available on the patient that the user is allowed to access
	5. The user updates the patient record, if needed, and closes the patient record
	6. The system both saves the changes to the patient record and adds a change record (if any changes); then closes the patient record and returns the user to the system overview
## Report Change of Patient Condition
- Actors: Nurse
- Goal: Update the patient condition in the system
- Main Flow:
	1. The nurse accesses the patient record as per the use case _Access or Change Patient Record_
	2. The nurse updates the patient condition
	3. The nurse closes the patient record and is returned to the system overview, as per the use case _Access or Change Patient Record_
## Report Change of Medication Need
- Actors: Nurse
- Goal: Update the patients medication need
- Main Flow:
	1. The nurse accesses the patient record as per the use case _Access or Change Patient Record_
	2. The nurse updates the patients medication need
	3. The nurse closes the patient record and is returned to the system overview, as per the use case _Access or Change Patient Record_
## Issue Urgent Care Instruction
- Actors: Doctor
- Goal: Record in the system that a patient needs urgent attention
- Main Flow:
	1. The doctor selects "Patient Requires Urgent Care"
	2. The system prompts for the patient name or ID
	3. The doctor enters the patient name or ID and submits the urgent care instruction
	4. The system stores and confirms the urgent care instruction and returns the doctor to the overview page
## Adjust Treatment Plan
- Actors: Doctor
- Goal: Adjust the treatment of a patient
- Main Flow:
	1. The doctor accesses the patient record as per the use case _Access or Change Patient Record_
	2. The doctor updates the patient treatment plan
	3. The doctor closes the patient record and is returned to the system overview, as per the use case _Access or Change Patient Record_