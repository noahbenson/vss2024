# Registration


<noscript><a href="https://www.eventbrite.com/e/{{page.eventbrite}}" rel="noopener noreferrer" target="_blank">You can buy tickets on Eventbrite, here.</a></noscript>

<button id="eventbrite-widget-modal-trigger-863420974377" type="button">Buy Tickets</button>

<script src="https://www.eventbrite.com/static/widgets/eb_widgets.js"></script>

<script type="text/javascript">
    var exampleCallback = function() {
        console.log('Order complete!');
    };
    window.EBWidgets.createWidget({
        widgetType: 'checkout',
        eventId: '{{page.eventbrite}}',
        modal: true,
        modalTriggerElementId: 'eventbrite-widget-modal-trigger-{{page.eventbrite}}',
        onOrderComplete: exampleCallback
    });
</script>

Registration fees are $10 for students, $20 for postdocs, and $50 for principal
investigators. All fees will go toward providing a computing environment for the
workshop, and participants will maintain access to that environment, including
all tutorials and lecture materials, for at least one month following the
conclusion of VSS.

Please contact [Noah Benson](mailto@nben.net) if you need to request a fee waiver.
