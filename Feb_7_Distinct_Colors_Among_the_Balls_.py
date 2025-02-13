def queryResults(limit: int, queries):
    ball_tracking, color_count = {},{}
    return_ans, ans = [],  0
    for ball, color in queries:
        if ball not in ball_tracking:
            ball_tracking[ball] = color
            if color not in color_count or (color in color_count and color_count[color] == 0):
                color_count[color] = 1
                ans+=1
                return_ans.append(ans)
            else:
                color_count[color] +=1
                return_ans.append(ans)
        else:
            prev_color = ball_tracking[ball]
            color_count[prev_color]-=1
            if color_count[prev_color] == 0:
                if color not in color_count or (color in color_count and color_count[color] == 0):
                    color_count[color] = 1
                    return_ans.append(ans)

                else:
                    color_count[color] += 1
                    ans-=1
                    return_ans.append(ans)
            else:
                if color not in color_count or (color in color_count and color_count[color] == 0):
                    color_count[color] = 1
                    ans+=1
                    return_ans.append(ans)
                else:
                    color_count[color] +=1
                    return_ans.append(ans)


            ball_tracking[ball] = color

    return return_ans



print(queryResults(4, [[0,1],[1,2],[2,2,],[3,4],[4,5]])) #[1,2,2,3,4]