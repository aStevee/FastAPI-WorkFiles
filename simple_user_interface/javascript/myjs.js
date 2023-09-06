console.log("Hello world!");


// This is a test, then remove this function please



function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a file to upload");
        return;
    }

    const formData = new FormData();
    formData.append('uploadedFile', file);

    fetch("http://127.0.0.1:8000/send_file/", {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log("Response: ",data);
        document.getElementById("messageLoad").textContent = `Document ${data.result} has been uploaded successfully`;
        document.getElementById("messageLoad").style = "color:green;";

    })
    .catch(error => {
        console.error('Error:', error);
        if (error == "TypeError: Failed to fetch"){
            document.getElementById("messageLoad").textContent = "You can only upload documents .json, .csv and .xlsx";
            document.getElementById("messageLoad").style = "color:red;";
        } else {
            document.getElementById("messageLoad".textContent = "Error detected: " + error);
            document.getElementById("messageLoad").style = "color:red;";
        }
            
    });
}


// Table maker

