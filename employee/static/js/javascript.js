function recon_pass() {
	if(document.getElementById('pass').value !=document.getElementById('recon').value)
	{
		alert("Passwords do not match");
		document.getElementById('recon').focus();
		return false;
	}
}