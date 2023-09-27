def get_scores_data(scores_list):
  highest_score = max(scores_list)
  lowest_score = min(scores_list)
  return highest_score, lowest_score
scores = [31, 17, 80]
data = get_scores_data(scores)
highest = data[0]
smallest = data[1]
print(f"smallest score: {smallest}")
print(f"highest score: {highest}")