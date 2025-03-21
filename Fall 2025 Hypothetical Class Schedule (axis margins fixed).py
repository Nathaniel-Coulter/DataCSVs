# Fall 2025 Hypothetical Class schedule (axis margins fixed)

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

def plot_schedule():
    
    courses = [
        ("Statistics and Data Analytics", "Monday", "5:00pm", "7:00pm", "#B03A2E"),
        ("Machine Learning for Everyone", "Tuesday", "10:40am", "12:05pm", "#2874A6"),
        ("Machine Learning for Everyone", "Friday", "10:40am", "12:05pm", "#2874A6"),
        ("Securities Analysis & Portfolio Mgt", "Tuesday", "1:50pm", "4:40pm", "#1D8348"),
        ("Managing Investment Funds", "Wednesday", "1:50pm", "4:40pm", "#B7950B"),
    ]
    
    def time_to_hours(time_str):
        time, meridian = time_str[:-2], time_str[-2:]
        hours, minutes = map(int, time.split(":"))
        if meridian.lower() == "pm" and hours != 12:
            hours += 12
        if meridian.lower() == "am" and hours == 12:
            hours = 0
        return hours + minutes / 60
    
    fig, ax = plt.subplots(figsize=(10, 6))
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    times = np.arange(9, 21, 1)  
    
    ax.set_xticks(np.arange(len(days)))
    ax.set_xticklabels(days, fontsize=12, fontweight='bold', ha='center')
    ax.set_yticks(times)
    ax.set_yticklabels([f"{(t-1)%12+1}:00 {'AM' if t<12 else 'PM'}" for t in times], fontsize=10)
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.invert_yaxis()  
    
    ax.xaxis.set_label_position('top')
    ax.xaxis.tick_top()
    ax.set_xlabel("Day of the Week", fontsize=12, fontweight='bold', labelpad=10)
    
    for course, day, start, end, color in courses:
        start_time = time_to_hours(start)
        end_time = time_to_hours(end)
        
        day_idx = days.index(day)
        ax.add_patch(plt.Rectangle((day_idx - 0.4, start_time), 0.8, end_time - start_time, 
                                   color=color, alpha=0.8))
    
    ax.set_ylabel("Time", fontsize=12, fontweight='bold')
    
    
    ax.set_ylim(9, 20)  
    
    fig.subplots_adjust(top=0.90, bottom=0.05, left=0.1, right=0.95)  
    
    patches = [mpatches.Patch(color=color, label=course) for course, _, _, _, color in courses]
    ax.legend(handles=patches, loc="lower center", fontsize=9, ncol=2, bbox_to_anchor=(0.5, -0.12))
    
    plt.show()

plot_schedule()