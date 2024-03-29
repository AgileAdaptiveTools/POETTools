import datetime

from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return u"%s the place" % self.name

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField()
    serves_pizza = models.BooleanField()

    def __unicode__(self):
        return u"%s the restaurant" % self.name

class ItalianRestaurant(Restaurant):
    serves_gnocchi = models.BooleanField()

    def __unicode__(self):
        return u"%s the italian restaurant" % self.name

class ParkingLot(Place):
    # An explicit link to the parent (we can control the attribute name).
    parent = models.OneToOneField(Place, primary_key=True, parent_link=True)
    capacity = models.IntegerField()

    def __unicode__(self):
        return u"%s the parking lot" % self.name

class ParkingLot2(Place):
    # In lieu of any other connector, an existing OneToOneField will be
    # promoted to the primary key.
    parent = models.OneToOneField(Place)

class ParkingLot3(Place):
    # The parent_link connector need not be the pk on the model.
    primary_key = models.AutoField(primary_key=True)
    parent = models.OneToOneField(Place, parent_link=True)

class Supplier(models.Model):
    restaurant = models.ForeignKey(Restaurant)

class Wholesaler(Supplier):
    retailer = models.ForeignKey(Supplier,related_name='wholesale_supplier')

class Parent(models.Model):
    created = models.DateTimeField(default=datetime.datetime.now)

class Child(Parent):
    name = models.CharField(max_length=10)

class SelfRefParent(models.Model):
    parent_data = models.IntegerField()
    self_data = models.ForeignKey('self', null=True)

class SelfRefChild(SelfRefParent):
    child_data = models.IntegerField()

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    class Meta:
        ordering = ('-pub_date', 'headline')

    def __unicode__(self):
        return self.headline

class ArticleWithAuthor(Article):
    author = models.CharField(max_length=100)

class M2MBase(models.Model):
    articles = models.ManyToManyField(Article)

class M2MChild(M2MBase):
    name = models.CharField(max_length=50)

class Evaluation(Article):
    quality = models.IntegerField()

    class Meta:
        abstract = True

class QualityControl(Evaluation):
    assignee = models.CharField(max_length=50)

class BaseM(models.Model):
    base_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.base_name

class DerivedM(BaseM):
    customPK = models.IntegerField(primary_key=True)
    derived_name = models.CharField(max_length=100)

    def __unicode__(self):
        return "PK = %d, base_name = %s, derived_name = %s" \
                % (self.customPK, self.base_name, self.derived_name)

class AuditBase(models.Model):
    planned_date = models.DateField()

    class Meta:
        abstract = True
        verbose_name_plural = u'Audits'

class CertificationAudit(AuditBase):
    class Meta(AuditBase.Meta):
        abstract = True

class InternalCertificationAudit(CertificationAudit):
    auditing_dept = models.CharField(max_length=20)

# Check that abstract classes don't get m2m tables autocreated.
class Person(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class AbstractEvent(models.Model):
    name = models.CharField(max_length=100)
    attendees = models.ManyToManyField(Person, related_name="%(class)s_set")

    class Meta:
        abstract = True
        ordering = ('name',)

    def __unicode__(self):
        return self.name

class BirthdayParty(AbstractEvent):
    pass

class BachelorParty(AbstractEvent):
    pass

class MessyBachelorParty(BachelorParty):
    pass

# Check concrete -> abstract -> concrete inheritance
class SearchableLocation(models.Model):
    keywords = models.CharField(max_length=256)

class Station(SearchableLocation):
    name = models.CharField(max_length=128)

    class Meta:
        abstract = True

class BusStation(Station):
    bus_routes = models.CommaSeparatedIntegerField(max_length=128)
    inbound = models.BooleanField()

class TrainStation(Station):
    zone = models.IntegerField()
