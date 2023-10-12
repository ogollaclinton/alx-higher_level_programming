#!/usr/bin/python3

if __name__ == "__main__":
        """Prints names defined by hidden_4 module."""
    import hidden_4

    hid = dir(hidden_4)
    for hid in hid:
        if hid[:2] != "__":
            print(hid)
