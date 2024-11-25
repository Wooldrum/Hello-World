import os
import time
import subprocess
import shutil

languages = [
    {"language": "Python", "extension": ".py", "command": "python"},
    {"language": "JavaScript", "extension": ".js", "command": "node"},
    {"language": "Java", "extension": ".java", "command": "javac HelloWorld.java && java HelloWorld"},
    {"language": "C++", "extension": ".cpp", "command": "g++ -o hello_world hello_world.cpp && hello_world"},
    {"language": "C#", "extension": ".cs", "command": "dotnet run --project CSharpHelloWorld"},
    {"language": "Ruby", "extension": ".rb", "command": "ruby"},
    {"language": "PHP", "extension": ".php", "command": "php"},
    {"language": "Swift", "extension": ".swift", "command": "swift"},
    {"language": "Kotlin", "extension": ".kt", "command": "kotlinc hello_world.kt -include-runtime -d hello_world.jar && java -jar hello_world.jar"},
    {"language": "R", "extension": ".R", "command": "Rscript"},
    {"language": "TypeScript", "extension": ".ts", "command": "tsc hello_world.ts && node hello_world.js"},
    {"language": "Go", "extension": ".go", "command": "go run"},
    {"language": "Rust", "extension": ".rs", "command": "rustc hello_world.rs && hello_world"},
    {"language": "SQL", "extension": ".sql", "command": "sqlite3 < hello_world.sql"}
]

code_snippets = {
    "Python": "print('Hello, World!')",
    "JavaScript": "console.log('Hello, World!');",
    "Java": "public class HelloWorld { public static void main(String[] args) { System.out.println(\"Hello, World!\"); } }",
    "C++": "#include <iostream>\nusing namespace std;\nint main() { cout << \"Hello, World!\" << endl; return 0; }",
    "C#": "using System;\nclass Program { static void Main() { Console.WriteLine(\"Hello, World!\"); } }",
    "Ruby": "puts 'Hello, World!'",
    "PHP": "<?php echo 'Hello, World!'; ?>",
    "Swift": "print(\"Hello, World!\")",
    "Kotlin": "fun main() { println(\"Hello, World!\") }",
    "R": "cat('Hello, World!\\n')",
    "TypeScript": "console.log('Hello, World!');",
    "Go": "package main\nimport \"fmt\"\nfunc main() { fmt.Println(\"Hello, World!\") }",
    "Rust": "fn main() { println!(\"Hello, World!\"); }",
    "SQL": "SELECT 'Hello, World!';"
}

for lang in languages:
    lang_name = lang["language"]
    extension = lang["extension"]
    command = lang["command"]
    filename = f"hello_world{extension}"

    with open(filename, "w") as file:
        file.write(code_snippets[lang_name])

    if lang_name == "C#":
        if not os.path.exists("CSharpHelloWorld"):
            subprocess.run("dotnet new console -o CSharpHelloWorld", shell=True)
            with open("CSharpHelloWorld/Program.cs", "w") as cs_file:
                cs_file.write(code_snippets["C#"])
        command = "dotnet run --project CSharpHelloWorld"

    if lang_name == "Java":
        os.rename(filename, "HelloWorld.java")
        filename = "HelloWorld.java"

    print(f"Running {lang_name} script...")
    try:
        if "&&" in command:
            subprocess.run(command, shell=True, check=True)
        else:
            subprocess.run(f"{command} {filename}", shell=True, check=True)
    except FileNotFoundError:
        print(f"{lang_name} interpreter/compiler not found. Please install it.")
    except Exception as e:
        print(f"Error running {lang_name}: {e}")

    time.sleep(5)

print("Waiting 10 seconds before cleanup...")
time.sleep(10)

for lang in languages:
    extension = lang["extension"]
    filename = f"hello_world{extension}"
    try:
        os.remove(filename)
        print(f"Deleted file: {filename}")
    except FileNotFoundError:
        print(f"File not found (already removed?): {filename}")
    except Exception as e:
        print(f"Error deleting file {filename}: {e}")

if os.path.exists("CSharpHelloWorld"):
    try:
        shutil.rmtree("CSharpHelloWorld")
        print("Deleted CSharpHelloWorld project folder.")
    except Exception as e:
        print(f"Error deleting CSharpHelloWorld folder: {e}")
