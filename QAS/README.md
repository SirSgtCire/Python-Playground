# Quality Assurance Strategies


## Installation and Usage

1. Install all external requirements for QAS.
2. Clone the repository and [install requirements](https://github.com/SirSgtCire/Python-Playground/blob/develop/QAS/requirements.txt)
3. Generate your own virtual environment using venv, following the readme for Python-Playground
4. Run the application with pytest: `pytest -s"`

NOTE: The application uses a `default.json` config file on invoking the code as
listed above. If you want to run the application with custom configuration,
then make your own json config file to load and give it as input:
`pytest -s --cfgfile your_cfg_file.json"`


## Automation Strategy

Having dedicated software to test applications as they grow is crucial to any company. QA automation enables software 
quality assessments and predictive data science implementations by giving human-readable programmatic access to the 
system under test. My core strategy for approaching QA automation is as follows:

1. Document and review the product workflow - understand the ins and outs of the system under test.
2. Write and review an initial test plan - identify and generate test cases that need to be run on the system under test daily, which includes system monitoring and system logging.
3. Write test framework - if using Python, create a main.py to use for invoking fixtures, and create fixtures as they arise in coding.
4. Integrate the test framework to the system under test - make sure given proper configs that the system under test is properly seen by the test framework.
5. Deploy test framework - once deployed, the automation framework should be able to report on all associated components within the system under test, whether that be console logging, SQL validation, Selenium views, etc.

At this stage the QA framework should meet the following criteria:
a. it has a comprehensive readme included in GitHub (installation and usage instructions, links to documentation for the system under test, and proper contact information for reaching out to the correct department).
b. anyone with proper authentication who pulls it down should be able to spin it up and use it by following the readme
c. it runs daily without error within its workings AND successfully identifies and reports on existing errors known within the system

6. Identify edge case scenarios for the system under test - we need to explore all use case scenarios of the system under test if we truly intend to create a solid product/platform, so we must use the system in ways we would never want to use the system and understand how the system under test will behave. Only when we have that understanding will we be able to write in necessary protection when needed, from a product perspective.
7. Write and review a test plan for each identified edge case scenario - we now need to implement each scenario independently and identify and report on the resulting behaviors of the system under test.
8. Implement each edge case scenario as a feature update to the QA framework - we need to ensure the framework keeps a clean history in GitHub since we want to prove at each stage of growth that it operates as expected. A granular history allows for better tracking of product direction, QA frameworks included.
9. Create different groups of tests and assign appropriate schedules - the goal here is to only run certain tests when we need to, saving on the usage of multiple resources by implementing more expensive test scenarios less frequently.
10. Repeat the process from step 6 as the system under test grows - whenever a new feature is added to the system under test, we should have associated tests for any identified/discovered behaviors, thereby continuing the growth of both the system under test and its associated QA framework.
