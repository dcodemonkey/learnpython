import sqlite3


con = sqlite3.connect('youtube_videos.db')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL

               )
''')

def list_video():
    print("Listing all videos...")
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(video_id, new_name, time):
    cursor.execute("UPDATE videos SET name= ?," 
    "time= ? WHERE id = ?", (new_name, time, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    con.commit()


def main():
    while True:
        print("Youtube Manager Application with DB.")
        print("1. List all youtube videos: ")
        print("2. Add a youtube video: ")
        print("3. Update a youtube video details: ")
        print("4. Delete a youtube video: ")
        print("5. Exit the application: ")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_video()
        elif choice == '2':
            name = input('Enter the video name: ')
            time = input('Enter the video time: ')
            add_video(name, time)

        elif choice == '3':
            video_id = input('Enter video ID to update: ')
            name = input('Enter the video name: ')
            time = input('Enter the video time: ')
            update_video(video_id,name, time)
        elif choice == '4':
            video_id = input('Enter video ID to delete: ')
            delete_video(video_id,name, time)
        elif choice == '5':
            print("Thanks for using YouYube Video manager. Exiting!!!!")
            break
        else:
            print('Invalid Choice: ', choice)
    con.close()
if __name__ == "__main__":
    main()