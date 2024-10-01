# DevOps_Orchestration
Objective : Update the backend and orchestrate migrating the 2 apps and script to Kubernetes Clusters following best practices using the technologies in the instructions.

## Tasks and Solutions
### Task 1 
Add a new backend api:
  - ```/download_external_logs``` makes a call to external service's api.
  - The external download API is dummy api, _you may leave it blank,_ however it requires $EXTERNAL_INTGERATION_KEY to authenticate
  - the external api has multiple enviroments so the integration key varies by enviroment
#### Solution : 
- In the ```backend_api/app.py``` file, a new api called download_external_logs is added. It makes an authentication using the $EXTERNAL_INTGERATION_KEY.
- The authentication key can also be passed via environment variables but here we have passed it using the  $EXTERNAL_INTGERATION_KEY variable since it has only one environment. We can also import the key using  os.environ.get() object.
<img width="769" alt="image" src="https://github.com/user-attachments/assets/9230dddd-4e8f-4e33-835c-fa8d04af87eb">


### Task 2
Update the health check to fit the new archeticture

#### Solution
- We declare an array API_URLs and assign two values as seen in line number 6 below. These two values are the URLs to the APIs declared in the ```backend-api/app.py``` file.
- The URL is modified to match the localhost.
- We iterate through each value of the API_URLs and make a HTTP request.
- If the response is OK, i.e "200" then we echo the success message as reachable and health check passed and write it into the $LOG_FILE
- If the response is NOT OK, then we echo the failure message as unreachable, and the http_response and write it into the $LOG_FILE
<img width="716" alt="image" src="https://github.com/user-attachments/assets/e6357418-1cd1-41d4-b1e7-758000547d78">


### Task 3
Create Helm chart for the stack

#### Solution
The below Helm Chart has been created for the project.
- The Kubernetes manifest files are inside the ```templates``` directory namely ```deployment.yaml``` and ```service.yaml```
- The basic information about the chart is stored in ```Chart.yaml``` file.
- The values for the Kubernetes manifest files are stored in ```values.yaml``` file.

<img width="199" alt="image" src="https://github.com/user-attachments/assets/39e8ee03-7e67-46fc-a3ab-0fe73c46388d">
<img width="199" alt="image" src="https://github.com/user-attachments/assets/743ec60d-fce6-4611-9562-6c6f7b56f9d4">


### Task 4
Deployment via Ansible

#### Solution
- The Deployment of the application with Ansible is done using the ```deployment.yml``` file.
- We first build the two docker images with the corresponding Dockerfile located in backend_api and data_api directories respectively.
- We then install these images to the Kubernetes cluster using Helm Charts.
- We run the health_check.sh script to perform the health check.
- <img width="488" alt="image" src="https://github.com/user-attachments/assets/980153e3-c029-4b3d-8f95-d067e7ffe48d">


### Task 5
Monitoring Kubernetes Applications - Demonstrate how to monitor the node and Pod and container's resource utilization

#### Solution
- The Kubernetes node's resource utilization can be monitored using the command ```kubectl top node```
- The Kubernetes pod's resource utilization can be monitored using the command ```kubectl top pod```
- The Kubernetes container's resource utilization can be monitored using the command ```kubectl top pod --containers```


### Task 6
How to display only resource utilization for Pods with specific label (k8s-app=kube-Devops)

#### Solution
- To display only resource utilization for pods with specific label, we can use the command ```kubectl top pod -l kube-Devops```
