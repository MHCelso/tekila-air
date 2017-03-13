window.addEventListener('load', function()
{
	var addCustomerId = document.querySelectorAll("#addFlight");
	var customerId = document.querySelector("#idCustomer");

	for (var i = 0; i < addCustomerId.length; i++) {

		addCustomerId[i].addEventListener('click', function(){
			customerId.value = this.value;
		}, false);

	}
}, false);