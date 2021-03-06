# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Company(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100,null=True,blank=True)
    HouseLocation = models.CharField(max_length=100,null=True,blank=True)
    StreetAddressZip = models.CharField(max_length=100,blank=True,null=True)
    Street = models.CharField(max_length=100,null=True,blank=True)
    MailingAddressZip = models.CharField(max_length=100,null=True,blank=True)
    MailingAddressCity = models.CharField(max_length=100,null=True,blank=True)
    StreetZip = models.CharField(max_length=100,null=True,blank=True)
    Telephoneareacode = models.CharField(max_length=200,null=True,blank=True)
    TelephoneNo = models.CharField(max_length=200,null=True,blank=True)
    TelephoneExtention = models.CharField(max_length=200,null=True,blank=True)
    FaxAreaCode = models.CharField(max_length=100,null=True,blank=True)
    FaxNumber = models.CharField(max_length=50,null=True,blank=True)
    FaxExtension = models.CharField(max_length=50,null=True,blank=True)
    Internet = models.CharField(max_length=100,null=True,blank=True)
    Email = models.CharField(max_length=150,null=True,blank=True)
    Population = models.CharField(max_length=100,null=True,blank=True)
    NumberOfInhabitants = models.CharField(max_length=100,null=True,blank=True)
    CourtType = models.CharField(max_length=100,null=True,blank=True)
    CourtSeat = models.CharField(max_length=100,null=True,blank=True)
    Workbench1 = models.CharField(max_length=100,null=True,blank=True)
    Workbench2 = models.CharField(max_length=100,null=True,blank=True)
    Workbench3 = models.CharField(max_length=100,null=True,blank=True)
    Workbench4 = models.CharField(max_length=100,null=True,blank=True)
    WorkflowStatus = models.CharField(max_length=100,null=True,blank=True)
    Sorting = models.IntegerField(default=1,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)


    def __str__(self):              
        return self.Name

	 

class Department(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    CompanyId = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='depart',null=True,blank=True)
    DepartmentName = models.CharField(max_length=100,null=True,blank=True)
    HomeAddressLocation = models.CharField(max_length=100,blank=True,null=True)
    StreetAddressZip =  models.CharField(max_length=100,blank=True,null=True)
    StreetNumber = models.CharField(max_length=100,null=True,blank=True)
    MailingAddressZip = models.CharField(max_length=100,null=True,blank=True)
    MailingAddressCity = models.CharField(max_length=100,null=True,blank=True)
    Telephoneareacode = models.CharField(max_length=200,null=True,blank=True)
    TelephoneNo = models.CharField(max_length=200,null=True,blank=True)
    TelephoneExtention = models.CharField(max_length=200,null=True,blank=True)
    FaxAreaCode = models.CharField(max_length=100,null=True,blank=True)
    FaxNumber = models.CharField(max_length=50,null=True,blank=True)
    FaxExtension = models.CharField(max_length=50,null=True,blank=True)
    Sorting = models.IntegerField(default=1,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):              
        return self.DepartmentName





class Functions_Master(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    FunctionName = models.CharField(max_length=100,null=True,blank=True)
    M_Sing = models.CharField(max_length=100,null=True,blank=True)
    F_Sing = models.CharField(max_length=100,null=True,blank=True)
    M_Plu = models.CharField(max_length=100,null=True,blank=True)
    F_Plu = models.CharField(max_length=100,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):              
        return self.FunctionName


class Employee(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100,null=True,blank=True)
    FirstName = models.CharField(max_length=100,null=True,blank=True)
    LastName = models.CharField(max_length=100,blank=True,null=True)
    SiteStatus = models.CharField(max_length=100,null=True,blank=True)
    PositionWeight = models.FloatField(null=True,blank=True)
    EntryDate = models.DateTimeField(auto_now=True,blank=True)
    DateOfBirth = models.DateTimeField(auto_now=True,blank=True)
    Gender = models.CharField(max_length=10,null=True,blank=True)
    Nationality = models.CharField(max_length=100,null=True,blank=True)
    CompanyId = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='+',null=True,blank=True)
    DepartmentId = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='+',null=True,blank=True)
    FunctionId = models.ForeignKey(Functions_Master, on_delete=models.CASCADE, related_name='+',null=True,blank=True)
    AdditionalFunction = models.CharField(max_length=100,null=True,blank=True)
    SecondFunction = models.CharField(max_length=100,null=True,blank=True)
    SecondFunctionAdditional = models.CharField(max_length=100,null=True,blank=True)
    SecondFunctionEntryDate = models.DateTimeField(auto_now=True,blank=True)
    SecondFunctionCourt  = models.CharField(max_length=100,null=True,blank=True)
    SecondFunctionSeat  = models.CharField(max_length=100,null=True,blank=True)
    ThirdFunction = models.CharField(max_length=100,null=True,blank=True)
    ThirdFunctionAdditional = models.CharField(max_length=100,null=True,blank=True)
    TelephoneAreaCode = models.CharField(max_length=50,null=True,blank=True)
    FaxAreaCode = models.CharField(max_length=50,null=True,blank=True)
    TelephoneNumber = models.CharField(max_length=50,null=True,blank=True)
    FaxNumber = models.CharField(max_length=50,null=True,blank=True)
    TelephoneExtension = models.CharField(max_length=50,null=True,blank=True)
    FaxExtension = models.CharField(max_length=50,null=True,blank=True)
    Email = models.CharField(max_length=150,null=True,blank=True)
    Sorting = models.IntegerField(default=1,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):              
        return self.Title



class CourtSeat_Master(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    CourtSeat = models.CharField(max_length=100,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):              
        return self.CourtSeat




class CourtType_Master(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    CourtType = models.CharField(max_length=100,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):              
        return self.CourtType




class WorkBench1_Master(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    WorkBench = models.CharField(max_length=100,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):              
        return self.WorkBench



class WorkBench2_Master(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    WorkBench = models.CharField(max_length=100,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):              
        return self.WorkBench



class WorkBench3_Master(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    WorkBench = models.CharField(max_length=100,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):              
        return self.WorkBench



class WorkBench4_Master(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    WorkBench = models.CharField(max_length=100,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)
    
    def __str__(self):              
        return self.WorkBench



class WorkFlowStatus_Master(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    WorkFlowStatus  = models.CharField(max_length=100,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):              
        return self.WorkBench


class SiteStatus_Master(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    Status  = models.CharField(max_length=100,null=True,blank=True)
    Abbriviation = models.CharField(max_length=100,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):              
        return self.Status


class PositionWeight_Master(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    Percentage  = models.FloatField(null=True,blank=True)
    Weightage = models.CharField(max_length=100,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)


    def __str__(self):
        return self.Status


class Gender_Master(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    Gender = models.CharField(max_length=100,null=True,blank=True)
    Abbriviation = models.CharField(max_length=100,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.Status



class Country_Master(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    Country = models.CharField(max_length=100,null=True,blank=True)
    Active = models.IntegerField(default=1,null=True,blank=True)
    CreatedBy = models.IntegerField(null=True,blank=True)
    CreateDate = models.DateTimeField(auto_now_add=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.Status

class TABLE_AUDIT(models.Model):
  
    ID  = models.AutoField(primary_key=True)
    Table_Name = models.CharField(max_length=100,null=True,blank=True)
    Column_Name = models.CharField(max_length=100,null=True,blank=True)
    RecordID = models.IntegerField(null=True,blank=True)
    Old_Value = models.CharField(max_length=100,null=True,blank=True)
    New_Value = models.CharField(max_length=100,null=True,blank=True)
    ModifiedBy = models.IntegerField(null=True,blank=True)
    ModifiedDate = models.DateTimeField(auto_now=True,blank=True)


    def __str__(self):
        return self.Status


















	


