def ValuesInQuadrant(quadrant):
    match quadrant:
        case 1:
            print(f'quadrant {quadrant}: x in (0; INF); y in (0; INF)')
        case 2:
            print(f'quadrant {quadrant}: x in (-INF; 0); y in (0; INF)')
        case 3:
            print(f'quadrant {quadrant}: x in (-INF; 0); y in (-INF; 0)')
        case 4:
            print(f'quadrant {quadrant}: x in (0; INF); y in (-INF; 0)')


quadrant = 1
ValuesInQuadrant(quadrant)

quadrant = 3
ValuesInQuadrant(quadrant)