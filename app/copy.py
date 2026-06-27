'''if list(d) != []:
    if list(d1) != []:
        d.update(password=z)
        return redirect(prof)
    else:
        messages.info(request, 'current password incorrect...please enter correct password to proceed')
        return render(request, 'changepass.html')
else:
    messages.info(request, 'username incorrect...please enter correct username to proceed')
    return render(request, 'changepass.html')
else:
return render(request, 'changepass.html')'''


