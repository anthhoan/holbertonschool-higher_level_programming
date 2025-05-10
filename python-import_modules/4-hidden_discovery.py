#!/usr/bin/python3
<<<<<<< HEAD
#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    sorted_names = sorted(name for name in names if not name.startswith("__"))
    for name in sorted_names:
        print(name)
=======
import hidden_4

if __name__ == '__main__':
    def_names = dir(hidden_4)

    for i in range(len(def_names)):
        if def_names[i][:2] != '__':
            print(def_names[i])
>>>>>>> 4d043365c6c96ade53b8e89c619694b39736d2eb
