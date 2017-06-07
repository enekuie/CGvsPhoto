# get the path to the CGvsPhoto directory
import sys
sys.path.append('../')

from model import Model




# to change to your favorite database
database_path = '/home/nicolas/Database/level-design_raise_100/'

# to change to the format of your image
image_size = 100

# define a single-image classifier
clf = Model(database_path, image_size, config = 'Personal', filters = [4,8],
            batch_size = 50, feature_extractor = 'Stats')


# trains the classifier and test it on the testing set
clf.train(nb_train_batch = 100,
          nb_test_batch = 80, 
          nb_validation_batch = 40,
          show_filters = False)
