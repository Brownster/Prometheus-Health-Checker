import requests

prometheus_url = "http://localhost:9090"

# Retrieve the Prometheus configuration
config_url = prometheus_url + "/api/v1/status/config"
config_response = requests.get(config_url)
if config_response.status_code == 200:
    config = config_response.json()
    print("Prometheus configuration:")
    print(config)
else:
    print("Failed to retrieve Prometheus configuration: %s" % config_response.text)

# Retrieve the list of scrape targets
targets_url = prometheus_url + "/api/v1/targets"
targets_response = requests.get(targets_url)
if targets_response.status_code == 200:
    targets = targets_response.json().get('data', {}).get('activeTargets', [])
    print("Scrape targets:")
    for target in targets:
        print(target)
else:
    print("Failed to retrieve scrape targets: %s" % targets_response.text)

# Retrieve the list of active alerts
alerts_url = prometheus_url + "/api/v1/alerts"
alerts_response = requests.get(alerts_url)
if alerts_response.status_code == 200:
    alerts = alerts_response.json()
    print("Active alerts:")
    print(alerts)
else:
    print("Failed to retrieve active alerts: %s" % alerts_response.text)

# Retrieve the list of loaded rules
rules_url = prometheus_url + "/api/v1/rules"
rules_response = requests.get(rules_url)
if rules_response.status_code == 200:
    rules = rules_response.json()
    print("Loaded rules:")
    print(rules)
else:
    print("Failed to retrieve loaded rules: %s" % rules_response.text)

# Retrieve the Prometheus metadata
metadata_url = prometheus_url + "/api/v1/metadata"
metadata_response = requests.get(metadata_url)
if metadata_response.status_code == 200:
    metadata = metadata_response.json()
    print("Prometheus metadata:")
    print(metadata)
else:
    print("Failed to retrieve Prometheus metadata: %s" % metadata_response.text)
