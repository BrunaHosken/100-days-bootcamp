# Build a custom web scraper to collect data on things that you are interested in.

import requests
from bs4 import BeautifulSoup

url = 'https://www.nba.com/stats/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

card_divs = soup.select('.LeaderBoardCard_lbcWrapper__e4bCZ')

for card in card_divs:
    title = card.select_one('.LeaderBoardCard_lbcTitle___WI9J')
    rows = card.select('.LeaderBoardPlayerCard_lbpcTableRow___Lod5')
    if title and rows:
        print(f'------------------------------------------------------------------------------')
        print(f'Title: {title.text.strip()}')
    else:
        continue

    if rows:
        for row in rows:
            position_cell = row.select_one('.LeaderBoardPlayerCard_lbpcTableCell__SnM1o')
            player_cell = row.select_one('.LeaderBoardPlayerCard_lbpcTableLink__MDNgL')
            team_cell = row.select_one('.LeaderBoardPlayerCard_lbpcTeamAbbr__fGlx3')
            points_cell = row.select_one('.LeaderBoardWithButtons_lbwbCardValue__5LctQ a')

            if position_cell and player_cell and team_cell and points_cell:
                position = position_cell.text.strip('.')
                player = player_cell.text.strip()
                team = team_cell.text.strip()
                points = points_cell.text.strip()

                print(f'Position: {position}, Player: {player}, Team: {team}, Points: {points}')
