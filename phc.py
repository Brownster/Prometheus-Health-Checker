import requests
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Prometheus Status")

# Create the GUI elements
status_text = tk.Text(root, width=80, height=30)
status_text.pack()

prometheus_select = tk.Listbox(root, height=3)
prometheus_select.pack()

def update_status():
    # Retrieve the selected Prometheus instance
    selected_prometheus = prometheus_select.get(prometheus_select.curselection())

    # Retrieve the Prometheus configuration
    config_url = f"{selected_prometheus}/api/v1/status/config"
    config_response = requests.get(config_url)
    if config_response.status_code == 200:
        config = config_response.json()
        status_text.insert(tk.END, "Prometheus configuration:\n")
        status_text.insert(tk.END, f"{config}\n\n")
    else:
        status_text.insert(tk.END, f"Failed to retrieve Prometheus configuration: {config_response.text}\n\n")

    # Retrieve the list of scrape targets
    targets_url = f"{selected_prometheus}/api/v1/targets"
    targets_response = requests.get(targets_url)
    if targets_response.status_code == 200:
        targets = targets_response.json().get('data', {}).get('activeTargets', [])
        status_text.insert(tk.END, "Scrape targets:\n")
        for target in targets:
            status_text.insert(tk.END, f"{target}\n")
        status_text.insert(tk.END, "\n")
    else:
        status_text.insert(tk.END, f"Failed to retrieve scrape targets: {targets_response.text}\n\n")

    # Retrieve the list of active alerts
    alerts_url = f"{selected_prometheus}/api/v1/alerts"
    alerts_response = requests.get(alerts_url)
    if alerts_response.status_code == 200:
        alerts = alerts_response.json()
        status_text.insert(tk.END, "Active alerts:\n")
        status_text.insert(tk.END, f"{alerts}\n\n")
    else:
        status_text.insert(tk.END, f"Failed to retrieve active alerts: {alerts_response.text}\n\n")

    # Retrieve the list of loaded rules
    rules_url = f"{selected_prometheus}/api/v1/rules"
    rules_response = requests.get(rules_url)
    if rules_response.status_code == 200:
        rules = rules_response.json()
        status_text.insert(tk.END, "Loaded rules:\n")
        status_text.insert(tk.END, f"{rules}\n\n")
    else:
        status_text.insert(tk.END, f"Failed to retrieve loaded rules: {rules_response.text}\n\n")

    # Retrieve the Prometheus metadata
    metadata_url = f"{selected_prometheus}/api/v1/metadata"
    metadata_response = requests.get(metadata_url)
    if metadata_response.status_code == 200:
        metadata = metadata_response.json()
        status_text.insert(tk.END, "Prometheus metadata:\n")
        status_text.insert(tk.END, f"{metadata}\n\n")
    else:
        status_text.insert(tk.END, f"Failed to retrieve Prometheus metadata: {metadata_response.text}\n\n")

# Add the update button
update_button = tk.Button(root, text="Update Status", command=update_status)
update_button.pack()

# Add the Prometheus instances to the dropdown
prometheus_select.insert(tk.END, "http://localhost:9090")
prometheus_select.insert(tk.END, "http://my-other-prometheus-instance:9090")

# Start the main loop
root.mainloop()
