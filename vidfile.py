def main():
    num_vids = int(input("How many videos are there: "))

    vid_file = open("video.txt", "w")

    print("Enter the running times of each of the videos...")

    for count in range(1, num_vids+1):
        run_time = float(input("Video number " + str(count) + ": "))
        vid_file.write(str(run_time) + "\n") 

    vid_file.close()


main()
