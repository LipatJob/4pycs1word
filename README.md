# 4 Pycs 1 Word
 
# Preface to Checker/Reader

Machine Problem 2

Author: Job Lipat

Date Created: May 17, 2020

Notes:



## Responsibilities of Modules:

### Presentation Layer
| Module | Functionality |
| ------- | ------------- |
| [__ main __](__main__.py) | Entry Point of the program |
| [<*module*>ViewController](payroll/PayrollViewController.py) | Where the UI of the program is handled |


### Business Logic Layer
| Module | Functionality |
| -------| ------------- |
| [<*module*>ViewModel](payroll/PayrollViewModel.py) | The ViewModel is queried by the UI to get the necessary data. The ViewModel queries entities to get the necessary data. |
| [<*module*>EntityManager](payroll/PayrollEntityManager.py) | Collection of multiple types of entities/data objects. Structured Data |
| [<*module*>EntityManagerFactory](payroll/PayrollEntityManagerFactory.py) | Creates an EntityManager |
| [<*singular_entity_name*>Entity](payroll/entities/EmployeeEntity.py) | A singular data object |
| [<*plural_entity_name*>Entity](payroll/entities/EmployeesEntity.py) | A collection of a single type of entity/data object |
| [<*entity_name*>EntityView](payroll/entities/PayrollRecordEntityView.py) | A data object that is used to aid in presentation. Usually used to combine data from mutliple entities|


### Persistence Layer
| Module | Functionality |
| -------| ------------- |
| [FileBound](payroll/entities/filebound/FileBound.py) | Abstract class to provide file storage functionality |
| [FileBound<*entity_name*>Entity](payroll/entities/filebound/FileBoundEmployeesEntity.py) | A class that inherits FileBound and an Entity to provide file storage functionality for an entity |
| [FileDataHandler](data/FileDataHandler.py) | Encapsulates file reading and writing |

### Miscellaneous
| Module | Functionality |
| -------| ------------- |
| [CaseInsensitiveDict](lib/CaseInsensitiveDict.py) | A dictionary where the keys are case insensitive |
| [Helper](lib/Helper.py) | Helper functions to help UI |
| [FileEncoder](payroll/filestrategy/FileEncoder.py) | Converts row-value array to a row-value string |
| [FileParser](payroll/filestrategy/FileParser.py) | Converts row-value string to a row-value array |





## Instructions
1. Create a program that will simulate the 4 pics 1 word game.
2. The program will each level displays four pictures linked by one word.
3. The player's aim is to work out what the word is, from a set of letters given below the pictures.
4. For each correct answer, the player will receive 10 coins that will be added to his wallet. The player has an initial 100 coins in his wallet. Coins can be used to buy hint by revealing letters of the answer. One letter is worth 2 coins. The player may also opt to pass and move to the next picture costing him of 10 coins.
5. The program must record the players progress level number, coin amount and the current picture he’s working on by storing data into a text file.
6. The program must not repeat pictures that are already answered by the player.
7. Provide at least 50 pictures from 3 – 8 letter words.
You may download pictures from the internet.

