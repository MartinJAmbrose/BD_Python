from Dict05 import update_inventory


def deep_copy_inventory(inv, sh, sa):
    inv_copy = {}
    for k in inv:
        inv_copy[k] = inv[k]

    sh_copy = []
    for d in sh:
        nd = {}
        for k in d:
            nd[k] = d[k]
        sh_copy.append(nd)

    sa_copy = []
    for d in sa:
        nd = {}
        for k in d:
            nd[k] = d[k]
        sa_copy.append(nd)

    return inv_copy, sh_copy, sa_copy


run_cases = [
    (
        {"potion": 5, "elixir": 2},
        [{"potion": 3}, {"ether": 4}],
        [{"potion": 2}, {"ether": 1}],
        {"potion": 6, "elixir": 2, "ether": 3},
    ),
    (
        {},
        [{"apple": 2}, {"banana": 1}],
        [{"apple": 1}, {"orange": 5}],
        {"apple": 1, "banana": 1},
    ),
    (
        {"arrow": 1},
        [],
        [{"arrow": 5}],
        {"arrow": 0},
    ),
]

submit_cases = run_cases + [
    (
        {"gem": 2, "coin": 10},
        [],
        [],
        {"gem": 2, "coin": 10},
    ),
    (
        {"rope": 3},
        [{"rope": 2}, {"torch": 5}, {"rope": 1}],
        [{"torch": 2}],
        {"rope": 6, "torch": 3},
    ),
    (
        {"scroll": 0},
        [{"scroll": 1}],
        [{"scroll": 1}, {"scroll": 1}],
        {"scroll": 0},
    ),
    (
        {"bread": 4},
        [{"bread": 2}, {"cheese": 3}],
        [{"milk": 10}, {"cheese": 1}, {"bread": 5}],
        {"bread": 1, "cheese": 2},
    ),
    (
        {"a": 1, "b": 2},
        [{"c": 3}, {"a": 4}],
        [{"d": 100}, {"b": 1}, {"c": 1}],
        {"a": 5, "b": 1, "c": 2},
    ),
]


def test_case(inventory, shipments, sales, expected_output):
    print("---------------------------------")
    print("Input:")
    print(f"  inventory: {inventory}")
    print(f"  shipments: {shipments}")
    print(f"  sales:     {sales}")
    inv_copy, sh_copy, sa_copy = deep_copy_inventory(inventory, shipments, sales)

    result = update_inventory(inventory, shipments, sales)

    print("Expected:")
    print(f"  updated:   {expected_output}")
    print("Actual:")
    print(f"  updated:   {result}")

    ok_value = result == expected_output

    inputs_unchanged = (
        inventory == inv_copy and shipments == sh_copy and sales == sa_copy
    )

    if not inputs_unchanged:
        print("Warning: Inputs were mutated (they should not be)")

    if ok_value and inputs_unchanged:
        print("Pass")
        return True

    print("Fail")
    return False



def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for case in test_cases:
        correct = test_case(*case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()