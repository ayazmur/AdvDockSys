%Import QtWidgets/QtWidgetsmod.sip

%If (Qt_5_0_0 -)

namespace ads
{

/**
 * Manages focus styling of dock widgets and handling of focus changes
 */
class CDockFocusController : QObject
{
    %TypeHeaderCode
    #include <DockFocusController.h>
    %End
    
public:
	CDockFocusController(ads::CDockManager* DockManager);
	virtual ~CDockFocusController();

	void notifyWidgetOrAreaRelocation(QWidget* RelocatedWidget);
	void notifyFloatingWidgetDrop(ads::CFloatingDockContainer* FloatingWidget);
    ads::CDockWidget* focusedDockWidget() const;
    void setDockWidgetTabFocused(ads::CDockWidgetTab* Tab);
    void clearDockWidgetFocus(ads::CDockWidget* dockWidget);
    void setDockWidgetTabPressed(bool Value);

public slots:
	void setDockWidgetFocused(ads::CDockWidget* focusedNow);
    
}; // class DockFocusController
};
 // namespace ads
 
%End