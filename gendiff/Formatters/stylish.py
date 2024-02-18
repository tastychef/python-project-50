def make_stylish(diff: dict, depth=0) -> str:
    lines = []
    for dictionary in diff:
        if dictionary['operation'] == 'same':
            lines.append(
                dictionary, 'value',
                depth, sign='    '
            )

        if dictionary['operation'] == 'add':
            lines.append(
                dictionary, 'new',
                depth, sign='  + '
            )