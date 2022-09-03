from sys import stdin

input = stdin.readline

n = int(input())
color_paper = [input().rstrip().split() for _ in range(n)]
blue_paper, white_paper = 0, 0

def number_of_color_papers(papers):
    global blue_paper, white_paper

    if len(papers) <= 1:
        if papers[0][0] == '0':
            white_paper += 1
        elif papers[0][0] == '1':
            blue_paper += 1
        return

    is_blue, is_white = False, False

    for paper in papers:
        if '0' in paper:
            is_white = True
        if '1' in paper:
            is_blue = True

        if is_blue and is_white:
            break
    else:
        if is_white:
            white_paper += 1
        elif is_blue:
            blue_paper += 1
        return

    half = len(papers) // 2
    top = papers[:half]
    bottom = papers[half:]

    top_left = [item[:half] for item in top]
    top_right = [item[half:] for item in top]
    bottom_left = [item[:half] for item in bottom]
    bottom_right = [item[half:] for item in bottom]

    number_of_color_papers(top_left)
    number_of_color_papers(top_right)
    number_of_color_papers(bottom_left)
    number_of_color_papers(bottom_right)

number_of_color_papers(color_paper)

print(white_paper)
print(blue_paper)
