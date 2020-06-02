import tkinter as tk
from time import sleep

if __name__ == "__main__":
    main_window = tk.Tk()
    main_frame = tk.Frame(main_window)
    main_frame.pack()
    new_project_button = tk.Button(
        main_frame,
        text='Create new job',
        command=quit
    )
    new_project_button.pack()

    edit_project_button = tk.Button(
        main_frame,
        text='Edit existing job',
        command=quit
    )
    edit_project_button.pack()

    delete_job_button = tk.Button(
        main_frame,
        text='Delete job',
        command=quit
    )
    delete_job_button.pack()

    run_jobs_button = tk.Button(
        main_frame,
        text='Run jobs',
        command=quit
    )
    run_jobs_button.pack()

    main_window.mainloop()
