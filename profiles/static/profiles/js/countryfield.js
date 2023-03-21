// From CI Project Ado
// Get the currently selected country value from #id_default_country
let countrySelected = $('#id_default_country').val();

// If no country is selected, change text color of select element to light grey
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
};

// Add an event listener to #id_default_country
$('#id_default_country').change(function() {
    // When the selected value changes, update the 'countrySelected' variable to the new value
    countrySelected = $(this).val();

    // If no country is selected, change text color of select element to light grey
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        // if not, change the text color of the select element to black
        $(this).css('color', '#000');
    }
});