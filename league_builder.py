import csv
'''Program takes a csv file that includes 18 soccer players with different experience levels
and sorts them into 3 teams of equal experience and players. Program then writes a txt file with the team rosters.'''

# Lists to hold players of different experience levels to later be sorted into teams.
players = []
experience = []
no_experience = []

# Lists for teams. 
dragons = []
sharks = []
raptors = []

def reader(players): # Function to read the csv file.
	with open('soccer_players.csv') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		rows = list(reader)
		for row in rows:
			players.append(dict(row)) # Iterates over the list and adds the player info as dicts into the player list.


def team_sorter(players, experience, no_experience): # Function to separate the players into 2 lists based on experience level.
	for player in players:
		if player['Soccer Experience'] == 'YES':
			experience.append(player)
		elif player['Soccer Experience'] == 'NO':
			no_experience.append(player)


def sort_experience(player, experience): # Function to add 3 experienced players to each team.
	for player in experience:
		if len(dragons) < 3: 
			dragons.append(player) # Stops adding when team has 3 experienced players.
		elif len(sharks) < 3:
			sharks.append(player)
		elif len(raptors) < 3:
			raptors.append(player)


def sort_no_experience(player, no_experience): # Function to add 3 inexperienced players to each team.
	for player in no_experience:
		if len(dragons) < 6:
			dragons.append(player) # Stops adding when team is full.
		elif len(sharks) < 6:
			sharks.append(player)
		elif len(raptors) < 6:
			raptors.append(player)

def team_writer(dragons, sharks, raptors): # Function for creating a txt file and writing the team roster to it in the desired format. 
		with open('teams.txt', 'a') as file:
			file.write('Dragons' + '\n')
			for player in dragons:
				file.write(
					player['Name'] 
					+ ', ' 
					+ player['Soccer Experience'] 
					+ ', ' 
					+ player['Guardian Name(s)'] 
					+ '\n'
					)
		with open('teams.txt', 'a') as file:
			file.write('\n' + 'Sharks' + '\n')
			for player in sharks:
				file.write(
					player['Name'] 
					+ ', ' 
					+ player['Soccer Experience'] 
					+ ', ' 
					+ player['Guardian Name(s)'] 
					+ '\n'
					)
		with open('teams.txt', 'a') as file:
			file.write('\n' + 'Raptors' + '\n')
			for player in raptors:
				file.write(
					player['Name'] 
					+ ', ' 
					+ player['Soccer Experience'] 
					+ ', ' 
					+ player['Guardian Name(s)'] 
					+ '\n'
					)	

if __name__ == "__main__": # Dunder name = Dunder main call to prevent program from running unintended if imported.
	reader(players)
	team_sorter(players, experience, no_experience)
	sort_experience(players, experience)
	sort_no_experience(players, no_experience)
	team_writer(dragons, sharks, raptors)
		