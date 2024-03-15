# Registration

Registration fees are $10 for students, $20 for postdocs, and $50 for principal
investigators. All fees will go toward providing a computing environment for the
workshop, and participants will maintain access to that environment, including
all tutorials and lecture materials, for at least one month following the
conclusion of VSS.

Please contact [Noah Benson](mailto:nben@nben.net) if you need to request a fee waiver.

<div id="eventbrite-widget-container-{{site.eventbrite}}"></div>

<script src="https://www.eventbrite.com/static/widgets/eb_widgets.js"></script>

<script type="text/javascript">
    var exampleCallback = function() {
        console.log('Order complete!');
    };

    window.EBWidgets.createWidget({
        // Required
        widgetType: 'checkout',
        eventId: '{{site.eventbrite}}',
        iframeContainerId: 'eventbrite-widget-container-{{site.eventbrite}}',

        // Optional
        iframeContainerHeight: 900,  // Widget height in pixels. Defaults to a minimum of 425px if not provided
        onOrderComplete: exampleCallback  // Method called when an order has successfully completed
    });
</script>
