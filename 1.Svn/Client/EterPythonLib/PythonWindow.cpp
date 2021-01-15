///Add
#include "../UserInterface/Locale_inc.h"

//Find in void CButton::OnMouseOverIn()
		PyCallClassMemberFunc(m_poHandler, "ShowToolTip", BuildEmptyTuple());
		
///Add
#if defined(ENABLE_DETAILS_UI)
		PyCallClassMemberFunc(m_poHandler, "OnMouseOverIn", BuildEmptyTuple());
#endif

//Find in void CButton::OnMouseOverOut()
		PyCallClassMemberFunc(m_poHandler, "HideToolTip", BuildEmptyTuple());
		
///Add
#if defined(ENABLE_DETAILS_UI)
		PyCallClassMemberFunc(m_poHandler, "OnMouseOverOut", BuildEmptyTuple());
#endif