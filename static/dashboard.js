let countdownTimers = {};
startCounters();

// Convert UTC Date to Local Date
function convertUTCDateToLocalDate(date) {
    var utcDate = new Date(date + 'Z');
    return new Date(utcDate.getTime()).toString();
}
<<<<<<< HEAD
=======

>>>>>>> 02185a2 (updated)
// Start the countdown for all environments
function startCounters() {
    const records = document.getElementsByClassName('timeRemaining');
    for (let i = 0; i < records.length; i++) {
        let hours = records[i].dataset.hours;
        let startTime = records[i].dataset.startTime;
        let env = records[i].dataset.env;
        if (hours && startTime) {
            startTime = convertUTCDateToLocalDate(startTime);
            startCountdown(startTime, hours, env);
        }
    }
}
<<<<<<< HEAD
=======

>>>>>>> 02185a2 (updated)
// Add hours to a given date
function addHours(date, hours) {
    date.setHours(date.getHours() + hours);
    return date;
}
<<<<<<< HEAD
=======

>>>>>>> 02185a2 (updated)
// Start the countdown timer for a specific environment
function startCountdown(startTime, hours, env) {
    const countdownDisplay = document.getElementById(`countdownDisplay-${env}`);
    if (countdownTimers[env]) {
        clearInterval(countdownTimers[env]); // Clear any existing timer for this environment
    }

    const endTime = addHours(new Date(startTime), parseInt(hours));
<<<<<<< HEAD

    countdownTimers[env] = setInterval(() => {
        const timeRemaining = endTime - Date.now();

    if (timeRemaining <= 0) {
    clearInterval(countdownTimers[env]);
    // alert("Time's up ! ");
    autoReleaseEnvironment(env);  // ← This triggers the actual backend release
    return;
 }
=======
    const displayCountdown = () => {
        const timeRemaining = endTime - Date.now();

        if (timeRemaining <= 0) {
            clearInterval(countdownTimers[env]);
            autoReleaseEnvironment(env);  // ← This triggers the actual backend release
            return;
        }
>>>>>>> 02185a2 (updated)


        let h = Math.floor(timeRemaining / 1000 / 60 / 60);
        let m = Math.floor((timeRemaining / 1000 / 60) % 60);
<<<<<<< HEAD
        let s = Math.floor((timeRemaining / 1000) % 60);

        h = h.toString().padStart(2, '0');
        m = m.toString().padStart(2, '0');
        s = s.toString().padStart(2, '0');

        countdownDisplay.textContent = `${h}:${m}:${s}`;
    }, 1000);
=======

        h = h.toString().padStart(2, '0');
        m = m.toString().padStart(2, '0');

        countdownDisplay.textContent = `${h}:${m}`;
    }
    displayCountdown(); // Initial call to set the countdown immediately
    countdownTimers[env] = setInterval(() => {
       displayCountdown();
    }, 60000);
>>>>>>> 02185a2 (updated)
}

function autoReleaseEnvironment(envName) {
    fetch(`/return/${envName}`, {
        method: 'POST'
    })
<<<<<<< HEAD
    .then(response => {
        if (response.ok) {
            console.log(`Auto-released: ${envName}`);
            
            const row = document.getElementById(`row-${envName}`);
            if (row) {
                row.classList.remove('grey-out');

                const actionCell = row.querySelector('td:last-child');
                actionCell.innerHTML = `<button onclick="openPopup('${envName}');" class="btn btn-success">Checkout</button>`;

                const countdownCell = document.getElementById(`countdownDisplay-${envName}`);
                countdownCell.textContent = "";

                row.querySelectorAll('td')[2].textContent = '';  // assign_to
                row.querySelectorAll('td')[3].textContent = '';  // comment
                row.querySelectorAll('td')[4].textContent = '';  // time
            }
        } else {
            console.error(`Failed to auto-release ${envName}`);
        }
    })
    .catch(err => {
        console.error(`Error auto-releasing ${envName}:`, err);
    });
=======
        .then(response => {
            if (response.ok) {
                console.log(`Auto-released: ${envName}`);

                const row = document.getElementById(`row-${envName}`);
                if (row) {
                    row.classList.remove('grey-out');

                    const actionCell = row.querySelector('td:last-child');
                    actionCell.innerHTML = `<button onclick="openPopup('${envName}');" class="btn btn-success">Checkout</button>`;

                    const countdownCell = document.getElementById(`countdownDisplay-${envName}`);
                    countdownCell.textContent = "";

                    row.querySelectorAll('td')[2].textContent = '';  // assign_to
                    row.querySelectorAll('td')[3].textContent = '';  // comment
                    row.querySelectorAll('td')[4].textContent = '';  // time
                }
            } else {
                console.error(`Failed to auto-release ${envName}`);
            }
        })
        .catch(err => {
            console.error(`Error auto-releasing ${envName}:`, err);
        });
>>>>>>> 02185a2 (updated)
}


// Function to open the popup
function openPopup(value) {
    document.getElementById('popup').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
    document.getElementById('env-value').value = value;
    document.getElementById('comment').focus();
}

// Function to close the popup
function closePopup(event) {
    event.preventDefault();
    document.getElementById("comment").value = '';
    document.getElementById('popup').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
<<<<<<< HEAD
}

document.addEventListener('DOMContentLoaded', () => {
    const hoursSelect = document.getElementById('hoursSelect');

    let autoSelected = false;

    hoursSelect.addEventListener('focus', () => {
        if (autoSelected) return;  
        
        autoSelected = true; 
    });

    hoursSelect.addEventListener('blur', () => {

        autoSelected = false;
    });
});
=======
}
>>>>>>> 02185a2 (updated)
