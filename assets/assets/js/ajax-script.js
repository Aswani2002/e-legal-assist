// Enhanced Contact Form Handler
const form = document.querySelector("form.form-contact");
const statusTxt = form.querySelector(".out-message");
const submitBtn = form.querySelector('button[type="submit"]');

// Utility function to show status messages
function showStatus(message, type = 'info') {
	const colors = {
		success: '#2ecc71',
		error: '#e74c3c',
		info: '#3498db'
	};
	
	statusTxt.style.color = colors[type] || colors.info;
	statusTxt.style.display = 'inline-block';
	statusTxt.innerText = message;
}

// Utility function to disable/enable form
function toggleFormState(disabled) {
	if (disabled) {
		form.classList.add('disabled');
		submitBtn.disabled = true;
	} else {
		form.classList.remove('disabled');
		submitBtn.disabled = false;
	}
}

// Client-side validation
function validateForm(formData) {
	const email = formData.get('email');
	const message = formData.get('message');
	const name = formData.get('name');
	
	if (!name || name.trim().length < 2) {
		showStatus('Please enter a valid name (at least 2 characters)', 'error');
		return false;
	}
	
	if (!email || !email.trim()) {
		showStatus('Email address is required', 'error');
		return false;
	}
	
	const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	if (!emailRegex.test(email)) {
		showStatus('Please enter a valid email address', 'error');
		return false;
	}
	
	if (!message || message.trim().length < 10) {
		showStatus('Message must be at least 10 characters long', 'error');
		return false;
	}
	
	return true;
}

// Form submission handler
form.onsubmit = async (e) => {
	e.preventDefault();
	
	const formData = new FormData(form);
	
	// Client-side validation
	if (!validateForm(formData)) {
		return;
	}
	
	showStatus('Sending your message...', 'info');
	toggleFormState(true);
	
	try {
		const response = await fetch('message.php', {
			method: 'POST',
			body: formData
		});
		
		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`);
		}
		
		const result = await response.text();
		
		// Check for error messages in response
		const errorMessages = [
			'Email and message field is required!',
			'Enter a valid email address!',
			'Sorry, failed to send your message!',
			'Invalid request method'
		];
		
		const hasError = errorMessages.some(msg => result.includes(msg));
		
		if (hasError) {
			showStatus(result, 'error');
		} else {
			showStatus(result, 'success');
			form.reset();
			
			// Hide success message after 5 seconds
			setTimeout(() => {
				statusTxt.style.display = 'none';
			}, 5000);
		}
	} catch (error) {
		console.error('Error:', error);
		showStatus('Network error. Please check your connection and try again.', 'error');
	} finally {
		toggleFormState(false);
	}
};

// Optional: Add input validation feedback on blur
const emailInput = form.querySelector('input[name="email"]');
if (emailInput) {
	emailInput.addEventListener('blur', () => {
		const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
		if (emailInput.value && !emailRegex.test(emailInput.value)) {
			emailInput.style.borderColor = '#e74c3c';
		} else {
			emailInput.style.borderColor = '';
		}
	});
}