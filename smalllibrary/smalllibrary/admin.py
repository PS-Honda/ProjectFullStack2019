from django.contrib import admin
from .models import Bindding,Book,Borrow,Pubilsher,Transaction,User

@admin.register(Bindding)
class BinddingAdmin(admin.ModelAdmin) :
    list_display = [f.name for f in Bindding._meta.fields]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin) :
    list_display = [f.name for f in Book._meta.fields]

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin) :
    list_display = [f.name for f in Borrow._meta.fields]
    
@admin.register(Pubilsher)
class PubilsherAdmin(admin.ModelAdmin) :
    list_display = [f.name for f in Pubilsher._meta.fields]

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin) :
    list_display = [f.name for f in Transaction._meta.fields]



admin.register(Bindding,BinddingAdmin)
admin.register(Book,BookAdmin)
admin.register(Borrow,BorrowAdmin)
admin.register(Pubilsher,PubilsherAdmin)
admin.register(Transaction,TransactionAdmin)
#admin.register(User,UserAdmin)