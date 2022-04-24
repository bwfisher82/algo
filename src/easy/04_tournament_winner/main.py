def suboptimal(competitions, results):
    score = {}

    for result_index, teams in enumerate(competitions):
        if teams[0] not in score: score[teams[0]] = 0
        if teams[1] not in score: score[teams[1]] = 0
        if results[result_index] == 0: # home won
            score[teams[1]] += 3
        elif results[result_index] == 1: # away won
            score[teams[0]] += 3

    best_team = ""
    best_score = 0
    for team, score in score.items():
        if score > best_score:
            best_score = score
            best_team = team

    return best_team


def optimal(competitions, results):
    score = {}
    best_team = ""

    for result, game in enumerate(competitions):
        team_won = ""
        if results[result] == 0:
            team_won = game[1]
        elif results[result] == 1:
            team_won = game[0]

        if team_won in score:
            score[team_won] += 3
        else:
            score[team_won] = 3

        if not best_team:
            best_team = team_won
        else:
            if score[team_won] > score[best_team]:
                best_team = team_won

    return best_team


def main():
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]
    results = [0, 0, 1]
    # print(suboptimal(competitions, results))
    return optimal(competitions, results)


if __name__ == "__main__":
    main()
